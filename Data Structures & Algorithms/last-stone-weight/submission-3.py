import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-el for el in stones]
        heapq.heapify(s)
        while len(s) > 1:
            x, y = heapq.heappop(s), heapq.heappop(s)
            delta = x - y
            if delta != 0:
                heapq.heappush(s, delta)
        return - s[0] if len(s) > 0 else 0
