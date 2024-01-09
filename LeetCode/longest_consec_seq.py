# import heapq as hq

# def longest_consec_seq(arr):
#     if len(arr) == 0:
#         return 0
#     if len(arr) == 1:
#         return 1
#     hq.heapify(arr)
#     subs = []
#     sub = [hq.heappop(arr)]
#     while arr:
#         root = hq.heappop(arr)
#         if root - sub[-1] == 1:
#             sub += [root]
#         else:
#             subs += [sub]
#             if arr:
#                 sub = [hq.heappop(arr)]
#             else:
#                 break
                
#     return len(max(subs,key=len))



def longest_consec_seq(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

print(longest_consec_seq([100, 4, 200, 1, 3, 2]))
print(longest_consec_seq([20, 30, 40, 10, 5, 6, 7, 8, 9]))