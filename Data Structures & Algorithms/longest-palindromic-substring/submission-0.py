class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 0
        result = ''

        for i in range(len(s)):

            # even_length

            j = i 
            k = i + 1

            print(j, k)

            while j >= 0 and k < len(s) and s[j] == s[k]:
                ans = max(ans, k - j + 1)
                if k - j + 1 == ans:
                    result = s[j: k + 1]


                j -= 1
                k += 1
              
           


            # odd length

            j = k = i

            while j >= 0 and k < len(s) and s[j] == s[k]:
                ans = max(ans, k - j + 1)
                if k - j + 1 == ans:
                    result = s[j: k + 1]


                j -= 1
                k += 1
                
            
        print(s)
        return result

            
        