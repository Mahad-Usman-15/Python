# return:It is used to return a statement with a function
import requests
import asyncio

def add(a,b):
    return a+b

sum=add(13,45)
print(sum)


def greet(name):
    if isinstance(name,str):
        return 'Valid name'
    else:
        return "Not a valid name"

    
print(greet("Mahad Usman"))    



def greet(name):
    if type(name)==str:
        return 'Valid name'
    else:
        return "Not a valid name"

    
print(greet("Mahad Usman"))



def products(url):
    response = requests.get(url)
    products = response.json()
    return products


getproducts=asyncio.run(products("https://jsonplaceholder.typicode.com/todos"))    
print(getproducts)