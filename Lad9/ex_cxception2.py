"""
Name : Anutta Thongdet
ID : 364411760003
Group : MIT421
"""

# Exception
print("Start")
while True :
    try :
     num = int(input("Enter an integer:"))
     print(f'Your number is {num}')
     break
    except ValueError as e:
     print("Error log:",e.args)
     print("Please, enter only integer.")

print("End")