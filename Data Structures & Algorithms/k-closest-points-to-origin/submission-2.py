class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        tuples, ans = [], []
        for x1, y1 in points:
            distance_to_origin = (x1 ** 2 + y1 ** 2) ** .5

            tuples.append((distance_to_origin, x1, y1))

        heapq.heapify(tuples)

        
        
        for _ in range(k):
            curr = heapq.heappop(tuples)
            curr_x, curr_y = curr[1], curr[2]
            ans.append([curr_x, curr_y])
        return ans

       
        