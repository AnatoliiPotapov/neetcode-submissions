from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque()
        index = 0
        output = [0] * numCourses
        num_prereq = [0] * numCourses
        is_dep = {}
        
        # заполнить список пререквизитов
        for to, prereq in prerequisites:
            num_prereq[to] += 1
            value = is_dep.get(prereq, [])
            value.append(to)
            is_dep[prereq] = value

        # заполнить кью вершинами в которых 
        for i in range(numCourses):
            if num_prereq[i] == 0:
                queue.append(i)

        # выполнить сам алгоритм заполняя
        while queue:
            elem = queue.popleft()
            for i in is_dep.get(elem, []):
                num_prereq[i] -= 1
                if num_prereq[i] == 0:
                    queue.append(i)

            output[index] = elem
            index += 1

        return index == numCourses

