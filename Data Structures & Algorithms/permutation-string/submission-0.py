class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        ref = {}
        perms = {}

        for i, letter in enumerate(s1):
            _other = s2[i]
            ref[letter] = ref.get(letter, 0) + 1
            perms[_other] = perms.get(_other, 0) + 1
        
        if ref == perms:
            return True

        left = 0
        for i in range(len(s1), len(s2)):
            
            letter = s2[i]

            perms[s2[left]] -= 1
            if perms[s2[left]] == 0:
                del perms[s2[left]]
            
            left += 1

            perms[letter] = perms.get(letter, 0) + 1

            print(perms)

            if perms == ref:
                return True
        return False



        
        




        
        