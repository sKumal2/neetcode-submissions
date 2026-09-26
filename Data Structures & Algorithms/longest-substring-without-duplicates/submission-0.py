class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create a window, and check for duplicates
        #return the length of the window 
        window = set()
        l = 0 
        max_window = 0
        for i in range(len(s)):

            while s[i] in window:
                window.remove(s[l])
                l += 1 

            window.add(s[i])

            max_window = max(max_window, i - l + 1)

        return max_window

