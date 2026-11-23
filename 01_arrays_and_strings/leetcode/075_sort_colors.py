# LeetCode 75 - Sort Colors (Medium)
# Technique: Dutch National Flag
# https://leetcode.com/problems/sort-colors/


class Solution:
    def sortColors(self, nums):
        right = len(nums)
        
        for i in range(right):
            for j in range(i, right):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    
