# LeetCode 49 - Group Anagrams (Medium)
# Technique: Hashing
# https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs):
        
        meta = dict()
        anagram_list = []
        index = 0
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in meta:
                anagram_list[meta[sorted_string]].append(string)
            else:
                meta[sorted_string] = index
                anagram_list.append([string])
                index += 1
        
        return anagram_list
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(sol.groupAnagrams([""]))