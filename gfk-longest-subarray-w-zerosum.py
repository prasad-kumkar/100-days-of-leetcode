# https://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/

def maxLen(nums):
    max_res = 0
    for num in range(len(nums)):
        start, end = num, len(nums)-1
        while start <= end:
            #print(nums[start:end+1])
            if sum(nums[start:end+1]) == 0:
                max_res = max(max_res, end+1-start)
            end-=1
    return max_res


nums = [1,0,3]
print(maxLen(nums), 5)