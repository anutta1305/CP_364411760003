"""
Name : Anutta Thongdet
ID : 364411760003
Group : MIT421
"""

def division(a,b):
    try:
        return a/b
    except:
        raise ZeroDivisionError("divide by zero")

try:
    rs = division(10,0)
    print("The result:",rs)
except Exception as e:
    print("Error log:",e.args)

print("End")

