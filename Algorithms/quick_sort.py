"""
Soltion By chat gpt
"""
def quick_sort(arr):
    """
    Sorts the input array using the Quick Sort algorithm.
    
    Args:
    - arr: Input list to be sorted.
    
    Returns:
    - Sorted list.
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:

print(quick_sort([8, 3, 1, 0, 25,10, 2]))
