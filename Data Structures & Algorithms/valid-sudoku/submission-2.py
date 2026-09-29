class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [[set() for j in range(len(board)//3)] for i in range(len(board)//3)]
        vertical = [set() for i in range(len(board))]
        horizontal = [set() for i in range(len(board))]
        print(boxes)

        for h in range(len(board)):
            for v in range(len(board[h])):
                temp = board[h][v]
                if temp == ".":
                    continue
                if (temp in vertical[v]) or (temp in horizontal[h]) or (temp in boxes[h//3][v//3]):
                    return False
                else:
                    vertical[v].add(temp)
                    horizontal[h].add(temp)
                    boxes[h//3][v//3].add(temp)
        
        return True