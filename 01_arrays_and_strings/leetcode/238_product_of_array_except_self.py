# LeetCode 238 - Product of Array Except Self (Medium)
# Technique: Prefix Product
# https://leetcode.com/problems/product-of-array-except-self/

import numpy

class Solution:
    def productExceptSelf(self, nums):
        ans = numpy.ones(len(nums), dtype=numpy.int32)
        
        for i in range(len(nums)):
            temp = ans[i]
            ans = ans * nums[i]
            ans[i] = temp
        
        return ans.tolist()
            
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))
    print(sol.productExceptSelf([-1,1,0,-3,3]))
