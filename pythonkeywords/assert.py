import unittest
# assert	For debugging
x = "hello"

#if condition returns True, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye"


name = "Mahad"

assert  name!="Mahad","Name should be only mahad"


def add(a,b):
    return a+b


assert add(2, 3) == 5
assert add(-1, 1) == 0
assert add(0, 0) == 0
        
    
    