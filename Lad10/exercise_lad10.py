"""
Name : Anutta Thongdet
ID : 364411760003
Group : MIT421
"""

"""
ให้นักศึกษาเขียนตารางสูตรคูณลงในไฟล์ test3.txt
โดยการรับ intput
แม่สูตรคูณจากผู้ใช้มา 1 ตัวเลข
"""

num = int(input("Enter an integer: "))

try:
    f = open("C:\\Users\LabCom_MT-4\Desktop\\test3.txt","a")
    for x in range(1,13):
        f.write(f'{num} x {x} = {num*x}\n')
except:
    print("Cloud not found a file.")
finally:
    f.close()
    print("Done.")

