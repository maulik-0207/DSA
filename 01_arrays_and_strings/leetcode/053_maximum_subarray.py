# LeetCode 53 - Maximum Subarray (Medium)
# Technique: Kadane's Algorithm
# https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for x in nums[1:]:
            current_sum = max(x, current_sum + x)
            max_sum = max(max_sum, current_sum)

        return max_sum

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(sol.maxSubArray([1]))
    print(sol.maxSubArray([5,4,-1,7,8]))