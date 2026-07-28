# LeetCode 1 - Two Sum (Easy)
# Technique: Hashing / Two Pointers
# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        # Return an empty list if no solution is found
        return []
    
if __name__ == '__main__':
    sol = Solution()
    
    print(sol.twoSum([2,7,11,15], 9))
    print(sol.twoSum([3,2,4], 6))
    print(sol.twoSum([3,3], 6))
