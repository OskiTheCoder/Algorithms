"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []

    def generate_help(s, left, right):
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:
            generate_help(s + "(", left + 1, right)
        if right < left:
            generate_help(s + ")", left, right + 1)

    s = ""
    left = 0
    right = 0
    generate_help(s, left, right)
    return res
