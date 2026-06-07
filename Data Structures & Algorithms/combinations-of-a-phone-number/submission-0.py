class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

       

        dig_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        ans = []



        def backtrack(currphone, index):
            if index == len(digits):
                if currphone != "":
                    ans.append(currphone)
            
                return
            
            for letter in dig_to_char[digits[index]]:
                backtrack(currphone + letter, index + 1)
            
        
        backtrack('', 0)
        return ans



        