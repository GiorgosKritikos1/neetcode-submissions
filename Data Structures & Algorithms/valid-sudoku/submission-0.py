class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes= [set() for _ in range(9)];
        for i in range(len(board)):
            seen=set();
            seen2=set();
            for j in range(len(board[i])):
                if board[i][j]!=".":
                    if board[i][j] in seen:
                        return False;
                    else:
                        seen.add(board[i][j]);
                if board[j][i]!=".":
                    if board[j][i] in seen2:
                        return False;
                    else:
                        seen2.add(board[j][i]);
                if board[i][j]!=".":
                    box= ((i//3) * 3 )+ (j//3);
                    if board[i][j] in boxes[box]:
                        return False;
                    else:
                        boxes[box].add(board[i][j]);
                        
                
        return True;
                
                