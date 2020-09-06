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