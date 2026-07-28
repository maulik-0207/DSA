# LeetCode 11 - Container With Most Water (Medium)
# Technique: Two Pointers
# https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        
        areas = []
        
        while left < right:
            areas.append((right -  left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return max(areas)    


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
    print(sol.maxArea([1,1]))
    print(sol.maxArea([1,2]))
    print(sol.maxArea([1,2,4,3]))
