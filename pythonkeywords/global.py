# Global variable definition (module scope)
x = 10 

def modify_global():
    global x  # Declare that we are using the global 'x'
    x = 20    # This modifies the global 'x'

def print_x():
    print(x)  # This function can read 'x' without 'global'

modify_global()
print_x()
print(x)
