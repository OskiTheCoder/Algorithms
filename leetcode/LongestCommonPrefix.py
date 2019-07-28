"""
LeetCode #14

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ""
    elif len(strs) == 1:
        return strs[0]
    longest_prefix = strs[0]
    for i in range(1, len(strs)):
        curr_prefix = ""
        curr_string = strs[i]
        for j in range(0, len(longest_prefix)):
            if j >= len(curr_string) or curr_string[j] != longest_prefix[j]:
                break
            else:
                curr_prefix += curr_string[j]
        if curr_prefix == "":
            return ""
        if len(curr_prefix) <= len(longest_prefix):
            longest_prefix = curr_prefix
    return longest_prefix

