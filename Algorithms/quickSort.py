# def sort(arr):
#     quick_sort(arr, 0,len(arr)-1)
#     return arr

# def quick_sort(arr, s, p):

#     if s < p:
#         if arr[s] > arr[p]:
#             # make the swap and compare again
#             arr[s],arr[p-1],arr[p] = arr[p-1], arr[p], arr[s]
#             p -= 1
                
#         else:
#             # move to next element and compare againe
#             s += 1

#     # pivot is in place sort left and right list recursivly
#     quick_sort(arr, 0, p-1)
#     quick_sort(arr,p+1,len(arr)-1)

#     return arr
 

# print(sort([8,3,1,7,0,10,2]))


"""
Soltion By chat gpt
"""
def sort(arr):
    quick_sort(arr, 0, len(arr) - 1)
    return arr

def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1

print(sort([8, 3, 1, 7, 0, 10, 2]))
