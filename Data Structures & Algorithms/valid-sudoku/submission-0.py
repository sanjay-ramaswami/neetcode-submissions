class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       rows=[set() for i in range(9)] 
       cols=[set() for i in range(9)] 
       boxes=[set() for i in range(9)] 
       for r in range(9):
        for c in range(9):
            if board[r][c]==".":
                continue
            nums=board[r][c]
            box=(r//3)*3+(c//3)
            if(nums in rows[r]or
                nums in cols[c]or
                nums in boxes[box]):
                return False
            rows[r].add(nums)
            cols[c].add(nums)
            boxes[box].add(nums)
       return True


        