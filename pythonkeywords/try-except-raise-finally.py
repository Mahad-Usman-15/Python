# try:try	To make a try statement
# except:Used with exceptions, what to do when an exception occurs

def divide(a,b):
    try:
        quotient=a/b
        return int(quotient)
    except ZeroDivisionError:
        raise 
    finally:
        print("statement passed")

quotient=divide(6,0)
print(quotient)



