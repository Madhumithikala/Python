
# nums = [2, 5, 1, 3, 4, 7] 
# half = len(nums) // 2
# x = nums[:half]
# y = nums[half:]
# listfinal = []
# for i in range(half):
#     listfinal.append(x[i])
#     listfinal.append(y[i])
# print(listfinal)

#Shuffle the array 
def Shuffle(li):
    l=len(li)
    if l%2!=0:
        return "Invalid input"
    half=l//2
    x=li[:half]
    y=li[half:]
    listfinal=[]
    for i in range(half):
        listfinal.append(x[i])
        listfinal.append(y[i])
    return listfinal
li_1=[1,2,3,4,5,6]
li_2=[4,5,6,7,22,11,1,7]
print(Shuffle(li_1))
print(Shuffle(li_2))