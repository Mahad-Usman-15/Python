# async:Define an asynchronous function
# with:	Used to simplify exception handling
# as:It is used to create an alias
# await:	Wait for and get a result from an awaitable

import asyncio
import httpx
import time
async def fetchurl(client, url):
    """Fetches a single URL using the provided async client."""
    print(f"Starting fetch for: {url}")
    response =  await client.get(url)
    return f"Finished {url} with status {response.status_code}"


async def main():
 urls = [
        f"https://jsonplaceholder.typicode.com/todos/{i}" 
        for i in range(1, 11) # Generating 10 sample URLs
    ]
 async with httpx.AsyncClient() as client:
     tasks=[fetchurl(client,url) for url in urls]
     
     # asyncio.gather runs them all at once!
     results = await asyncio.gather(*tasks)
    #  The * (unpacking operator) tells Python to treat the list as individual arguments.
     for res in results:
        print(res)
        
        
if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    print(f"\nTotal time taken: {end_time - start_time:.2f} seconds")        
 