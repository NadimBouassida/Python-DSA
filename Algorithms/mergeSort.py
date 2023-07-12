def merge_sort(arr):
    if len(arr) <= 1:
        return arr 
    
    mid = len(arr) // 2
    arr_left = arr[:mid]
    arr_right = arr[mid:]
    
    sorted_left = merge_sort(arr_left)
    sorted_right = merge_sort(arr_right)
    
    return merge(sorted_left,sorted_right)


def merge(left, right):
    merged = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1

    merged.extend(right[r:])
    merged.extend(left[l:])
        
    return merged



print(merge_sort([8,3,1,7,0,10,2]))