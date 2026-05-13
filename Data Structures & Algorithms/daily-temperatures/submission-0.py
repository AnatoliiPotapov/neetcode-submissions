class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                j, _ = stack.pop()
                output[j] = i - j
            stack.append((i, temperatures[i]))
        return output