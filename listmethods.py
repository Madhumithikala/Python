# dict={}
# s=(1,2,3,4)
# for i in range(len(s)):
#     dict[i]=s[i]
# print(dict)

a= int(input(" Enter the list size:"))
li=[]
for i in range(1,a+1):
    b= int(input(" Enter the element:"))
    li.append(b) 
print(li)
options=("1.insert","2.delete","3.sorted","4.reverse","5.exit")
while True:
    choice=input(" Enter the  choose option:")
    if choice=="1":
        val=int(input(" Enter the number:"))
        li.append(val)
        print(li)
    elif choice=="2":
        val=int(input(" Enter the value to be deleted:"))
        li.remove(val)
        print(li)
    elif choice=="3":
        li.sort()
        print(li)
    elif choice=="4":
        li.reverse()
        print(li)
    elif choice=="5":
        print("Exit")
        break
    else:
        print(" Invalid ")
        