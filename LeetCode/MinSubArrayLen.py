from collections import deque

def minSubArrayLen(nums:list, target: int):
    n = len(nums)
    deq = deque()
    sum = 0
    minLen = float('inf')

    for i in range(n):
        # append current num
        deq.append(nums[i])
        # evaluate sum
        sum += nums[i]
        # check if the sum is bigger then the target
        if sum >= target:
            # keep removing nums from start to minimize length of list
            while sum - deq[0] >= target:              
                # remove first item from deq and update the sum accordinally
                sum -= deq.popleft()        
            # remeber the length
            minLen = min(minLen, len(deq))

    return 0 if minLen == float('inf') else minLen

print(minSubArrayLen([50,10,8,30,40,60,0,4,8], 70))