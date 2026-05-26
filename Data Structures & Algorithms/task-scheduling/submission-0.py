from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        heap = [(-cnt, val) for val, cnt in cnt.items()]
        heapq.heapify(heap)
        cooldown = deque()
        time = 0

        while heap or cooldown:
            time += 1

            if heap:
                elem = heapq.heappop(heap)
                
                if elem[0] < -1:
                    cooldown.append((elem[0] + 1, elem[1], time + n))
                    
            # check if I can return something from cooldown
            if cooldown:
                if cooldown[0][2] <= time:
                    el = cooldown.popleft()[:2]
                    heapq.heappush(heap, el)

        return time