def func1():
    print("Welcome to Day3 AI Class")
    
def func2():
    var1 = int(input("Enter the value of var1:"))
    var2 = int(input("Enter the value of var2:"))
    
    var3 = var1 + var2
    print("Addition:",var3)
    
def func3(var1, var2):
    var3 = pow(var1,var2)
    print("Pow:",var3)
    
def func4():
    var1 = int(input("Enter the value of var1:"))
    var2 = int(input("Enter the value of var2:"))
    var3 = var1 * var2
    var4 = var1/var2
    return (var3,var4)   

def func5(var1,var2):
    var3 = var1/var2
    return var3