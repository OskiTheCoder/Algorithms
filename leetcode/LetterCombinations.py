import itertools
"""
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []
    m = {}
    m['2'] = ['a', 'b', 'c']
    m['3'] = ['d', 'e', 'f']
    m['4'] = ['g', 'h', 'i']
    m['5'] = ['j', 'k', 'l']
    m['6'] = ['m', 'n', 'o']
    m['7'] = ['p', 'q', 'r', 's']
    m['8'] = ['t', 'u', 'v']
    m['9'] = ['w', 'x', 'y', 'z']

    chars = []
    for digit in digits:
        chars.append(m[digit])
    res = []
    for p in itertools.product(*chars):
        res.append(''.join(p))
    return res
