class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


        graph = defaultdict(list)

        for a, b, time in times:
            graph[a].append((time, b))
        
        dist = [float('inf')] * (n + 1)

        dist[k] = 0

        heap = [(0, k)] # distance, node

        while heap:
            curr_distance, curr_node = heapq.heappop(heap)

            for distance_to_other, other in graph[curr_node]:

                new_distance = curr_distance + distance_to_other

                if new_distance < dist[other]:
                    heapq.heappush(heap, (new_distance, other))

                    dist[other] = new_distance
                
        dist = dist[1:]
        return max(dist) if max(dist) != float('inf') else -1



        

        