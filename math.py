
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y              # on master

def multiply(x,y):
    return x*y          # on Bug456

def divide(x,y):
    if y==0:              #master
        return Error
    else:
        return x/y
  
def square(x,y):
   return x*x
