class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        stack = []

        def recurse(openCnt: int, closedCnt: int) -> None:
            if openCnt == closedCnt == n:
                output.append("".join(stack))
                return
            
            if openCnt < n:
                stack.append("(")
                recurse(openCnt+1, closedCnt)
                stack.pop()
            
            if closedCnt < openCnt:
                stack.append(")")
                recurse(openCnt, closedCnt+1)
                stack.pop()
        
        recurse(0, 0)
        return output