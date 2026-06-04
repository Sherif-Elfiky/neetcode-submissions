class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)

        sorted_counts = sorted(counter.items(), key = lambda x: x[1], reverse = True)

        sorted_counts = sorted_counts[:k]

        ans = [x[0] for x in sorted_counts]

        return ans
        