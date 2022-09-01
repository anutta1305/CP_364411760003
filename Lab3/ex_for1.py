"""
Name : Anutta Thongdet
ID : 364411760003
Group : MIT421
"""

# for loop

# range

for x in range(10): #0-9
    print(x,end=" ")

#1-10
for x in range(1,11):
    print(x,end=" ")

# แสดงตัวเลขตั้งแต่ 1-100 ที่หารด้วย 5 ลงตัว
for x in range (5,101,5):
    print(x,end=" ")

# แสดงตัวเลขตั้งแต่ 1-100 ที่หารด้วย 3 และ 5 ลงตัว
print(" ")
for x in range(1,101):
    if x%3==0 and x%5==00:
        print(x,end=" ")