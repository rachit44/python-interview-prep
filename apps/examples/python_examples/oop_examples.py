# apps/examples/python_examples/oop_examples.py
"""
Object-Oriented Programming Examples for Interview Preparation
"""

class Employee:
    """Basic Employee class demonstrating OOP concepts"""
    
    # Class variable
    company_name = "Tech Corp"
    employee_count = 0
    
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
        Employee.employee_count += 1
    
    def __str__(self):
        return f"Employee({self.name}, {self.department})"
    
    def __repr__(self):
        return f"Employee(name='{self.name}', salary={self.salary}, department='{self.department}')"
    
    def get_annual_salary(self):
        """Calculate annual salary"""
        return self.salary * 12
    
    @classmethod
    def from_string(cls, emp_str):
        """Alternative constructor from string"""
        name, salary, department = emp_str.split('-')
        return cls(name, int(salary), department)
    
    @staticmethod
    def is_workday(day):
        """Check if given day is a workday"""
        return day.weekday() < 5

class Manager(Employee):
    """Manager class demonstrating inheritance"""
    
    def __init__(self, name, salary, department, team_size):
        super().__init__(name, salary, department)
        self.team_size = team_size
    
    def get_annual_salary(self):
        """Override with manager bonus"""
        base_salary = super().get_annual_salary()
        bonus = base_salary * 0.1  # 10% bonus
        return base_salary + bonus
    
    def conduct_meeting(self):
        return f"{self.name} is conducting a team meeting"

class Developer(Employee):
    """Developer class with specific methods"""
    
    def __init__(self, name, salary, department, programming_languages):
        super().__init__(name, salary, department)
        self.programming_languages = programming_languages or []
    
    def add_skill(self, language):
        """Add a programming language skill"""
        if language not in self.programming_languages:
            self.programming_languages.append(language)
    
    def code_review(self, code_lines):
        """Simulate code review process"""
        return f"{self.name} reviewed {code_lines} lines of code"

# Design Patterns Examples

class Singleton:
    """Singleton pattern implementation"""
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.data = {}
            self._initialized = True

class DatabaseConnection(Singleton):
    """Database connection using Singleton pattern"""
    
    def connect(self):
        return "Connected to database"
    
    def execute_query(self, query):
        return f"Executing: {query}"

# Factory Pattern
class VehicleFactory:
    """Factory pattern for creating vehicles"""
    
    @staticmethod
    def create_vehicle(vehicle_type, **kwargs):
        if vehicle_type.lower() == 'car':
            return Car(**kwargs)
        elif vehicle_type.lower() == 'motorcycle':
            return Motorcycle(**kwargs)
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")

class Vehicle:
    """Base vehicle class"""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start_engine(self):
        return f"{self.brand} {self.model} engine started"

class Car(Vehicle):
    def __init__(self, brand, model, year, doors=4):
        super().__init__(brand, model, year)
        self.doors = doors
    
    def honk(self):
        return "Beep beep!"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_size):
        super().__init__(brand, model, year)
        self.engine_size = engine_size
    
    def wheelie(self):
        return "Performing a wheelie!"

# Observer Pattern
class Subject:
    """Subject in Observer pattern"""
    
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)
    
    def set_state(self, state):
        self._state = state
        self.notify()
    
    def get_state(self):
        return self._state

class Observer:
    """Observer base class"""
    
    def update(self, subject):
        raise NotImplementedError

class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name
    
    def update(self, subject):
        print(f"{self.name} received update: {subject.get_state()}")

