class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                tempIx, temp = stack.pop()
                res[tempIx] = i - tempIx
            stack.append((i, temperatures[i]))
        
        return res