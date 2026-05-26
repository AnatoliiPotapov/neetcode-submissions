import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for i, point in enumerate(points):
            dist = point[0]**2 + point[1]**2
            if len(heap) < k:
                heapq.heappush(heap, (-dist, i, point))
            else:
                heapq.heappushpop(heap, (-dist, i, point))
        return [el[2] for el in heap]

