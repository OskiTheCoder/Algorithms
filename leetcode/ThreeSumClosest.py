"""
LeetCode #16

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    curr_dist = -float('inf')
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[l] + nums[r] + nums[i] - target
            if abs(s) < abs(curr_dist):
                curr_dist = s
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                return target
    return target + curr_dist
