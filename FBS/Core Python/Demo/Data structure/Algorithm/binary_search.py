

def binarysearch(li, Search_ele):

    beg = 0
    end = len(li) - 1

    while beg <= end:

        mid = (beg + end) // 2

        if Search_ele == li[mid]:
            return mid

        elif Search_ele > li[mid]:
            beg = mid + 1

        elif Search_ele < li[mid]:
            end = mid - 1

    else:
        return -1


ele = 80
li = [10, 20, 30, 40, 50, 60]

res = binarysearch(li, ele)



if res != -1:
    print(f'{ele} is present at index {res}.')
else:
    print(f'{ele} is not present in list.')




