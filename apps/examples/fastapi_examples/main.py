# apps/examples/fastapi_examples/main.py
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, validator
from typing import List, Optional
from datetime import datetime
import asyncio

app = FastAPI(title="Interview Prep API Examples", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Models
class UserBase(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email address')
        return v

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class APIResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None

# In-memory database for demo
users_db = []
user_id_counter = 1

@app.get("/")
async def root():
    return {"message": "FastAPI Interview Examples API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now()}

# CRUD Operations Example
@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """Create a new user - demonstrates POST endpoint with validation"""
    global user_id_counter
    
    # Check if user already exists
    for existing_user in users_db:
        if existing_user['email'] == user.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists"
            )
    
    new_user = {
        "id": user_id_counter,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "created_at": datetime.now()
    }
    users_db.append(new_user)
    user_id_counter += 1
    
    return new_user

@app.get("/users/", response_model=List[UserResponse])
async def get_users(skip: int = 0, limit: int = 10):
    """Get all users with pagination - demonstrates GET with query parameters"""
    return users_db[skip: skip + limit]

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """Get user by ID - demonstrates path parameters and error handling"""
    for user in users_db:
        if user['id'] == user_id:
            return user
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id {user_id} not found"
    )

@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_update: UserBase):
    """Update user - demonstrates PUT endpoint"""
    for i, user in enumerate(users_db):
        if user['id'] == user_id:
            updated_user = user.copy()
            updated_user.update(user_update.dict(exclude_unset=True))
            users_db[i] = updated_user
            return updated_user
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id {user_id} not found"
    )

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    """Delete user - demonstrates DELETE endpoint"""
    for i, user in enumerate(users_db):
        if user['id'] == user_id:
            del users_db[i]
            return
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id {user_id} not found"
    )

# Async Operations Example
@app.get("/async-example/")
async def async_operation_example():
    """Demonstrates async/await usage in FastAPI"""
    async def fetch_data():
        await asyncio.sleep(1)  # Simulate I/O operation
        return {"data": "Fetched from external API"}
    
    async def process_data(data):
        await asyncio.sleep(0.5)  # Simulate processing
        return {"processed": data["data"].upper()}
    
    # Run operations concurrently
    data = await fetch_data()
    processed = await process_data(data)
    
    return {
        "message": "Async operations completed",
        "result": processed,
        "timestamp": datetime.now()
    }

# Dependency Injection Example
def get_api_key(api_key: str = None):
    """Simple API key dependency for demonstration"""
    if not api_key or api_key != "secret-key":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )
    return api_key

@app.get("/protected/")
async def protected_endpoint(api_key: str = Depends(get_api_key)):
    """Protected endpoint demonstrating dependency injection"""
    return {
        "message": "Access granted to protected resource",
        "api_key": api_key
    }

# Error Handling Example
@app.get("/error-example/{error_type}")
async def error_handling_example(error_type: str):
    """Demonstrates different types of error handling"""
    if error_type == "validation":
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Validation error example"
        )
    elif error_type == "not-found":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resource not found example"
        )
    elif error_type == "server":
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error example"
        )
    else:
        return {"message": f"No error for type: {error_type}"}


# apps/core/views