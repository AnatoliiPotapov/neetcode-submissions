import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        x = [-el for el in list(nums)]
        heapq.heapify(x)
        for i in range(k):
            el = heapq.heappop(x)
        return -el
        