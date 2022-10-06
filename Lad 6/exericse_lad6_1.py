"""
Name : Anutta Thongdet
ID : 364411760003
Group : MIT421
"""
# โปรแกรมเพื่อรับค่าอินพุตจากผู้ใช้เป็นเลขจำนวนเต็มจำนวน 2 ชุดข้อมูล โดยมีข้อมูลชุดละ 10 ตัว
#จากนั้นให้แสดงข้อมูลที่ซ้ำกัน และไม่ซ้ำกันจากข้อมูล 2 ชุดนี้
#ทางจอภาพ

s1 = set()
for i in range(10): #0-9
    x = int(input(f"enter an integer {i+1:}:"))
    s1.add(x)
print(s1)

s2 = set()
for i in range(5): #0-9
    x = int(int(f"set 2) enter an integer {i+1}: "))
    s2.add(x)
print(s2)

print("sam integer betweem s1 and s2:", s1.intersection(s2))
print("difference integer betweem s1 and s2:", s1.intersection(s2))



