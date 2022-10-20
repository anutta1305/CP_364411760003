"""
Name : Anutta Thongdet
ID : 364411760003
Group : MIT421
"""

# create file
#import os
create emty file
try :
    f = open("test2.txt","x")
except:
    print("File already exits.")

# create test3.txt on desktop of your computer
#C:\User\C:\Users\LabCom_MT-4\Destktop
try:
      f = open("C:\\Users\LabCom_MT-4\Desktop\\test3.txt","x")
except Exception as e:
    print(e)


# write file
# mode "a"
try :
    f = open("test2.txt","w")
    f.write("Anutta Thongdet\n")
except:
    print("Cloud not found a fine name 'test2.txt")
finally :
    f.close()

# delete file

if os.path.exists("test3.txt"):
    os.remove("test3.txt")
else:
    print("File not found.")