
# list=[0,1,1,0,1,0,1,0]
# one=list.count(1)
# zero=list.count(0)
# print(min(one,zero)*2)


subarray= int(input(" Enter the list size:"))
li=[]
for i in range(1,subarray+1):
    b= int(input(" Enter the element:"))
    li.append(b) 
one=li.count(1)
zero=li.count(0)
print(min(one,zero)*2)