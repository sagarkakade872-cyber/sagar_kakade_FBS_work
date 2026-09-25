def bubble_sorrt(li):
    size=len(li)
    for i in range(1,size):
        for j in range(0,size-i):
            if(li[j]>li[j+1]):
                li[j],li[j+1]=li[j+1],li[j]
li=[50,40,30,20,10]
print(li)
bubble_sorrt(li)                
print(li)


# # def bubble_sort(list):
# #     size = len(list)
# #     for i in range(1, size):
# #         for j in range(0, size-i):
# #             if(list[j] > list[j+1]):
# #                 list[j], list[j+1] = list[j+1], list[j]

# # list = [50, 40, 30, 20, 10]
# # print(list)
# # bubble_sort(list)
# # print(list)


# def bubble(li):
#     size=len(li)
#     for i in range (0,size):
#         for j in range (1,size-i):
#             if(li[j]<li[j+1]):
#              li[j], li[j+1]=li[j+1],li[j]      
# li=[50,40,30,20,10]             
# print(li)
# bubble(li)
# print










