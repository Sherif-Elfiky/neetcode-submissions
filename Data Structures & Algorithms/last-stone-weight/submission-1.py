class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        neg_stones = [-x for x in stones]
        heapq.heapify(neg_stones)

        while neg_stones:
            print(neg_stones)

            first_max = heapq.heappop(neg_stones)
            if not neg_stones:
                return -first_max
                break
            sec_max = heapq.heappop(neg_stones)

            if first_max != sec_max:
                new_val = abs(first_max - sec_max)
                heapq.heappush(neg_stones, -new_val)

        if not neg_stones:
            return 0

              





        