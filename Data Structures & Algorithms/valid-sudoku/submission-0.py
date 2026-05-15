class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        column = {}
        three = {}
        for i in range(len(board)):
            row.setdefault(i, [])
            for j in range(len(board[0])):
                column.setdefault(j, [])
                three.setdefault((i//3,j//3), [])
                
                print(f"{i}: I and {j} : J")
                if (board[i][j] == "."):
                    continue
                if (board[i][j] in row[i]):
                    print('row')
                    print(row)
                    print(column)
                    print(board[i][j])
                    return False
                
                if (column[j] and board[i][j] in column[j]):
                    print(f'col is {j}')
                    print(row)
                    print(column)
                    print(board[i][j])
                   
        
                    return False
                
                if (three[(i//3, j//3)] and board[i][j] in three[(i//3, j//3)]):
                    print(f'threes {i//3+j//3}')

                    print(three[(i//3, j//3)])
                    print(board[i][j])

                    return False

                row[i].append(board[i][j])
                column[j].append(board[i][j])
                three[(i//3, j//3)].append(board[i][j])
        print(row)
        print(column)
        print(three)
        return True
                