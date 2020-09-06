def foo():
    print("foo")

def bar():
    print("bar")

def baz():
    print("baz")

def qux():
   print("qux")

def myFunction(var):
    # Execute expression x for all elements x in var2 where x is of type list, and create a list from it
    # Dereference the list to get the list inside
    print(*[x for x in var if type(x) == list])

def FindType(var):
    varType = str(type(var))
    return varType[varType.find("'") + 1: varType.rfind("'")]

var1 = "Hello" 
var2 = list(var1)
var2.append(list("World"))
var2.append(["Hello", "World"])

myFunction(var2)


var3 = [foo, bar, baz, qux]
[x() for x in var3]


var4 = 2
var5 = type(var4)
var6 = str(var5)
print(type(var5))
print(*[var4, "is of type: ", FindType(var4)])
print(*[var3[0], "is of type: ", FindType(var3[0])])

print("No args: " + str(type(foo)))
print("With args: " + str(type(myFunction)))

def printNumber(num):
    print(num)

import inspect
var3.append(printNumber)
# Call a function with argument `12` only if the function takes arguments
[x(12) for x in var3 if len(inspect.getfullargspec(x).args) != 0]


def noArgs():
    print("No arguments")

def oneArgs(arg1):
    print("One argument: " + str(arg1))

def twoArgs(arg1, arg2):
    print("Two arguments: " + str(arg1) + ", " + str(arg2))

def threeArgs(arg1, arg2, arg3):
    print("Three arguments: " + str(arg1) + ", " + str(arg2) + ", " + str(arg3))

import random

functionList = [*([noArgs] * 2), *([oneArgs] * 5), *([twoArgs] * 3), *([threeArgs] * 10)]
random.shuffle(functionList)

print(functionList)

# Generate a random integral argument value for each argument that a function takes in the list
[x(*(random.sample(range(0, 65535), len(inspect.getfullargspec(x).args)))) for x in functionList]
