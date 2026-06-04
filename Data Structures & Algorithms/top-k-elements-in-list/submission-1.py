class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        arr = []

        for key, v in counts.items():
            arr.append((-v, key))
        heapq.heapify(arr)
        ans = []
        for _ in range(k):
            curr_key = heapq.heappop(arr)[1]
            ans.append(curr_key)
        
        return ans



        



        
        