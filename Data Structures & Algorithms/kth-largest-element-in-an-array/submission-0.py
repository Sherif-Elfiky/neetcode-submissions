class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        new_arr = [-x for x in nums]

        heapq.heapify(new_arr)

        for _ in range(k):
            curr = heapq.heappop(new_arr)
        return -curr
        