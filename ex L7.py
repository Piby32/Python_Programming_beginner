def add(x, y):
    return x + y
def mul(x, y):
    return x * y
def mine(x, y):
    return x - y
def defi(x, y):
    return x / y
x = int(input("please input x : "))
y = int(input("please input y : "))
print("x+y=",add(x, y))
print("x*y=",mul(x, y))
print("x-y=",mine(x, y))
print("x/y=",defi(x, y))

******************************************************************************************************************************************************************************

def greet(ss="johndo "):
    print("Hello, world!"+ss)

greet()
greet("Piby"))

******************************************************************************************************************************************************************************

  def factorial(n):
    if n == 1:
        #print(n)
        return 1
    else:
        print(n)
    return factorial(n - 1)
    
print(factorial(3))
