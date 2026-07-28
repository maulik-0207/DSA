# LeetCode 3 - Longest Substring Without Repeating Characters (Medium)
# Technique: Sliding Window
# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s):
        last = {}   # char -> last index seen
        start = 0   # left boundary of current window
        max_len = 0

        for i, ch in enumerate(s):
            prev = last.get(ch, -1)
            if prev >= start:
                # character repeated inside current window -> move start
                start = prev + 1
            last[ch] = i
            # update max length
            if i - start + 1 > max_len:  # noqa: PLR1730
                max_len = i - start + 1

        return max_len

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
    print(sol.lengthOfLongestSubstring("bbbbb"))
    print(sol.lengthOfLongestSubstring("pwwkew"))