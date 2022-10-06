"""
Name : Anutta Thongdet
ID : 364411760003
Group : MIT421
"""

# function
# 1.build-in function
print("Hello , MIT421")
s = "RUTS"
print(len(s))

# 2.create by owner -- using "det" keyword

def myfunction1():
    print("Hello, from function 1.")

def myfunction2(msg):
    print("Hello, from funvtion 2" , msg)

def myfunction3(num1,num2):
    print("Hello, from function 3.")
    # return statement
    return  num1+num2

# calling function
myfunction1()

# calling function with parameter
myfunction2("RUTS")

# calling function with parameter and return statement
rs = myfunction3(10,10)
print(rs)

print(myfunction3(20,20))

