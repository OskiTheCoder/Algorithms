"""

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]


"""


def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    candidates.sort()
    dfs_help(candidates, target, res, [])
    return res


def dfs_help(candidates, target, res, arr):
    if target == 0:
        res.append(arr)
        return
    if target < 0:
        return
    if candidates == []:
        return
    for num in candidates:
        if num > target:
            break
        if arr and num < arr[-1]:
            continue
        else:
            dfs_help(candidates, target - num, res, arr + [num])
    return
