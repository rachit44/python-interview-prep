# apps/examples/python_examples/async_examples.py
"""
Async/Await Examples for Interview Preparation
"""

import asyncio
import aiohttp
import time
from concurrent.futures import ThreadPoolExecutor

async def fetch_data(url, session):
    """Async function to fetch data from URL"""
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        return f"Error fetching {url}: {str(e)}"

async def fetch_multiple_urls(urls):
    """Fetch multiple URLs concurrently"""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(url, session) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

async def producer(queue, items):
    """Producer coroutine for async queue"""
    for item in items:
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(0.1)  # Simulate work
    
    # Signal completion
    await queue.put(None)

async def consumer(queue, name):
    """Consumer coroutine for async queue"""
    while True:
        item = await queue.get()
        if item is None:
            # Signal received, stop consuming
            await queue.put(None)  # Re-add signal for other consumers
            break
        
        print(f"Consumer {name} consumed: {item}")
        await asyncio.sleep(0.2)  # Simulate processing
        queue.task_done()

async def async_context_manager_example():
    """Example of async context manager"""
    
    class AsyncResource:
        async def __aenter__(self):
            print("Acquiring async resource")
            await asyncio.sleep(0.1)
            return self
        
        async def __aexit__(self, exc_type, exc_val, exc_tb):
            print("Releasing async resource")
            await asyncio.sleep(0.1)
        
        async def do_work(self):
            print("Doing async work")
            await asyncio.sleep(0.1)
    
    async with AsyncResource() as resource:
        await resource.do_work()

def blocking_function(n):
    """Simulate blocking I/O operation"""
    time.sleep(n)
    return f"Processed {n} items"

async def run_blocking_in_executor():
    """Run blocking functions in thread executor"""
    loop = asyncio.get_event_loop()
    
    with ThreadPoolExecutor() as executor:
        # Run blocking functions concurrently
        tasks = [
            loop.run_in_executor(executor, blocking_function, 1),
            loop.run_in_executor(executor, blocking_function, 2),
            loop.run_in_executor(executor, blocking_function, 3),
        ]
        
        results = await asyncio.gather(*tasks)
        return results

class AsyncIterator:
    """Custom async iterator example"""
    
    def __init__(self, max_count):
        self.max_count = max_count
        self.current = 0
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.current >= self.max_count:
            raise StopAsyncIteration
        
        await asyncio.sleep(0.1)  # Simulate async work
        self.current += 1
        return self.current

async def async_generator():
    """Async generator example"""
    for i in range(5):
        await asyncio.sleep(0.1)
        yield i

# Performance comparison example
async def async_task(n):
    await asyncio.sleep(0.1)
    return n * 2

def sync_task(n):
    time.sleep(0.1)
    return n * 2

async def compare_sync_vs_async():
    """Compare synchronous vs asynchronous performance"""
    
    # Synchronous approach
    start_time = time.time()
    sync_results = [sync_task(i) for i in range(5)]
    sync_duration = time.time() - start_time
    
    # Asynchronous approach
    start_time = time.time()
    async_results = await asyncio.gather(*[async_task(i) for i in range(5)])
    async_duration = time.time() - start_time
    
    return {
        'sync_results': sync_results,
        'sync_duration': sync_duration,
        'async_results': async_results,
        'async_duration': async_duration
    }