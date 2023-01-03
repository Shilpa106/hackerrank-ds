def deco1(func):
    def inner1():
        print("hi inner 1")
        x=func()
        print("inner1 val of x",x)
        return x*x 
    
    return inner1

def deco2(func):
    def inner2():
        print("hi inner 2")
        x=func()
        print("inner2 x val",x)
        
        print("x*2 for deco2",x*2)
        return x*2 
    return inner2

@deco2
@deco1
def func():
    return 10 

print(func())
        