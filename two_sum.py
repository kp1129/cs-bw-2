# return indices of elements that add up to target int - leetcode

def two_sum(nums, target):
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums and nums.index(complement) != i:
            return [i, nums.index(complement)]
    

# https://leetcode.com/problems/two-sum/
