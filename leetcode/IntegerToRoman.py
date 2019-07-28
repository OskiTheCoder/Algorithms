"""
LeetCode #12

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999

"""


def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    roman = ""
    while num != 0:
        if num >= 1000:
            roman = roman + "M"
            num = num - 1000
        elif num >= 900:
            roman = roman + "CM"
            num = num - 900
        elif num >= 500:
            roman = roman + "D"
            num = num - 500
        elif num >= 400:
            roman = roman + "CD"
            num = num - 400
        elif num >= 100:
            roman = roman + "C"
            num = num - 100
        elif num >= 90:
            roman = roman + "XC"
            num = num - 90
        elif num >= 50:
            roman = roman + "L"
            num = num - 50
        elif num >= 40:
            roman = roman + "XL"
            num = num - 40
        elif num >= 10:
            roman = roman + "X"
            num = num - 10
        elif num >= 9:
            roman = roman + "IX"
            num = num - 9
        elif num >= 5:
            roman = roman + "V"
            num = num - 5
        elif num >= 4:
            roman = roman + "IV"
            num = num - 4
        else:
            roman = roman + "I"
            num = num - 1
    return roman
