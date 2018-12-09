"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    curr_max = nums[0]
    overall_max = nums[0]
    n = len(nums)
    for i in range(1, n):
        curr_max = max(nums[i], nums[i] + curr_max)
        overall_max = max(curr_max, overall_max)
    return overall_max
