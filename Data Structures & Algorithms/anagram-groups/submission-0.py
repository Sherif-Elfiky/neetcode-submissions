class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        def char_to_pos(character):
            return ord(character) - ord('a')

        vals = defaultdict(list)

        for word in strs:
            curr = [0] * 26
            for letter in word:

                curr[char_to_pos(letter)] += 1
            
            vals[tuple(curr)].append(word)

        return list(vals.values())
        


        