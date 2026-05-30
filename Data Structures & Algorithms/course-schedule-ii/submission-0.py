from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = [0] * numCourses
        inbound_count = [0] * numCourses
        index = 0
        is_prereq = defaultdict(list)
        queue = deque()

        for to, prerec in prerequisites:
            is_prereq[prerec].append(to)
            inbound_count[to] += 1

        for i in range(numCourses):
            if inbound_count[i] == 0:
                queue.append(i)

        while queue:
            elem = queue.popleft()
            output[index] = elem
            index += 1
            for i in is_prereq[elem]:
                inbound_count[i] -= 1
                if inbound_count[i] == 0:
                    queue.append(i)
        
        return output if index == numCourses else []
                

        



        