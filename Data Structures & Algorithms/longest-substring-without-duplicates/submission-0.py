class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        left = 0
        curr_set = set()
        ans = 0
        

        for right in range(len(s)):

            while s[right] in curr_set:
                curr_set.remove(s[left])
                left += 1
            
            curr_set.add(s[right])
            ans = max(ans, right - left + 1)

        return ans


        