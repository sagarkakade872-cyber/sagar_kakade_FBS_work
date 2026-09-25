# def search(li,search_ele):
#     size=len(li)
#     for ind in range (0,size):
#         if(li[ind]==search_ele):
#             return ind
#     else:
#         return -1
# ele=20
# li=[10,20,30,40,50,60]        
# res=search(li, ele) 
# print(res)
# if (res!=-1):
#     print(f"the number is in list")
# else:
#     print(f'number not in list')



def linear(list, serching_ele):
    size = len(list)
    for ind in range(0, size):
        if(list[ind] == serching_ele):
            return ind
    else:
        return -1

list = [10, 20, 30, 40, 50]
ele = 50
res = linear(list, ele)
print(res)        
