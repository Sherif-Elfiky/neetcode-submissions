class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

      
        for i in range(len(digits) - 1, -1, -1):

            if i == len(digits) - 1:
                digits[i] += 1
            
            if digits[i] >= 10:
                digits[i] -= 10

                if i - 1 < 0:
                    digits = [1] + digits
                else:
                    digits[i - 1] += 1
        return digits

            
        