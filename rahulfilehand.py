import os
def read():
    
    f1=open(r"D:\python\rahul shah\data.txt","r")
    data=f1.readlines()
    for i in data:
        print(i,end='')
def write():
    f=open(r"D:\python\rahul shah\data.txt","a")
    ans='y'
    while ans=='y':
        name=input("enetr name:  ")
        roll=int(input("enetr your roll number :   "))
        aim=input("enetr your aim:  ")
        st=[name,str(roll),aim]
        f.write(str(st))
        f.write('\n')
        ans=input("do you want to add more :  ")
        print("")
        print("")
        f.close()

print("1. read")
print("2. write")
print("3. rename")
print("4. remove")
ask=input("enter your choice:   ")
if ask=='2':
    write()
    print("")
    print("")
    anc=input(" do you want to read data :    ")
    if anc=='y':
        read()
    else:
        print("")
        print("successfully written")
elif ask=='1':
    read()
    print("")
    print("")
    anx=input(" do you want to add data :  ")
    if anx=='y':
        write()
    else:
        print("")
        print("")
        print("successfully read")
elif ask=='4':
    os.remove("D:\\python\\rahul shah\\data.txt")
elif ask=='3':
    renam=input("enter file name:   ")
    rename1="D:\\python\\rahul shah\\"+renam
    os.rename("D:\\python\\rahul shah\\data.tx",rename1)
else:
    print("")
    print("")
    print("invalid choice ...please choose r or a ")
    print("")
    
