# LeetCode 42 - Trapping Rain Water (Hard)
# Technique: Two Pointers / Stack
# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height):
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0
        trapped = 0

        while left < right:
            if height[left] <= height[right]:

                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    trapped += left_max - height[left]

                left += 1

            else:

                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    trapped += right_max - height[right]

                right -= 1

        return trapped
            
if __name__ == '__main__':
    sol = Solution()
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(sol.trap([4,2,0,3,2,5]))
    print(sol.trap([4, 2, 0, 3, 2]))
    print(sol.trap([4, 2, 3]))