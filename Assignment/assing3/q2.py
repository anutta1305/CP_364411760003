"""
Name : Anutta Thongdet
ID : 364411760003
Group : MIT421
"""

#เขียนฟังก์ชันเพื่อยกกำลังสองสมาชิกทุกตัวใน list และ return list ที่เป็นผลลัพธ์จากการยกกำลังสอง
#ออกมากำหนดให้ฟังก์ชันนี้รับ parameter 1 ตัว คือ listA ที่มีสมาชิกเป็นจำนวนใด ๆ

a = int(print("key1:"))
b = int(print("key2:"))
c = int(print("key3:"))

l = [a,b,c]
power = 2

for i in rang(len(l)):
    print(l[i],"ยกกำลัง",power,"เท่ากับ",power(l[i],power))

