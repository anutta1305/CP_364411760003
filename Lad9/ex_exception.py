"""
Name : Anutta Thongdet
ID : 364411760003
Group : MIT421
"""

# Exception
print("Start")

x = "MIT421"

try :
    print(x)
except NameError:
    print("variable ma,e not define.")
except :
    print("Something went wrong.")
else :
    print("No error.")
finally :
    print("Error has been excepted.")

print("End")