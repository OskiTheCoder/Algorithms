"""
LeetCode #20

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
"""


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    m = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in s:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if stack:
                top = stack.pop()
            else:
                top = ""
            if top != m[char]:
                return False
    return stack == []