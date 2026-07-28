"""
String Operations - Implement basic string operations manually
Operations: reverse(), isPalindrome(), isAnagram(str1, str2)
"""


def reverse_string(s):
    return s[::-1]


def is_palindrome(s):
    return s == s[::-1]


def is_anagram(s1, s2):
    anagram_dic = dict()  # noqa: C408
    for i in s1.lower():
        if i in anagram_dic:
            anagram_dic[i] += 1
        else:
            anagram_dic[i] = 1
    for i in s2.lower():
        if i in anagram_dic:
            anagram_dic[i] -= 1
        else:
            anagram_dic[i] = -1
    
    for key in list(anagram_dic.values()):
        if key < 0:
            return False
    
    return True

if __name__ == "__main__":
    # print(reverse_string("Maulik"))
    # print(reverse_string("A"))
    # print(reverse_string("ABC"))
    # print(reverse_string("AB"))
    
    # print(is_palindrome("Maulik"))
    # print(is_palindrome("ABA"))
    # print(is_palindrome("CIC"))
    
    
    print(is_anagram("Mau", "AUM"))
    print(is_anagram("ABC", "DFG"))
    print(is_anagram("BCD", "ABC"))
    print(is_anagram("XYZ", "yzx"))
