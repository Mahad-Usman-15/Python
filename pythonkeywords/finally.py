# finally
try:
    a=int(input("Enter any number"))
    print(a)
except Exception as e:
    raise
finally:
    print("Hello")  #This is where finally takes advantage.
       
       
try:
    a=int(input("Enter any number"))
    print(a)
except Exception as e:
    raise

print("Hello")  #This will not run.       