# accounts=[[1,2,3],[3,2,1,7]]
# max=0
# for i in accounts:
#     sum1=0
#     for j in i:
#         sum1+=j
#         if max<sum1:
#             max=sum1
# print(max)

def rich(li):
    max_wealth = 0
    for i in li:
        _sum = sum(i)
        if max_wealth < _sum:
            max_wealth = _sum
    return max_wealth

li_1 = [[1, 2, 3], [3, 2, 1, 7]]
print(rich(li_1))  

li_2 = [[1, 5], [7, 3], [3, 5]]
print(rich(li_2))  

li_3 = [[2, 8, 11], [3, 9, 8]]
print(rich(li_3))


