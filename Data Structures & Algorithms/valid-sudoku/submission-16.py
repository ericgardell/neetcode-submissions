from math import floor

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        subs = dict()
        for r in range(len(board)):
            print('new row', board[r], rows)
            for c in range(len(board[r])):
                val = board[r][c]
                if val == ".": 
                    pass
                else: 
                    print(f'cell r:{r}, c:{c}, val:{val}, row-set:{rows[r]}')
                    sector = f"r{floor(r/3)}c{floor(c/3)}"
                    if sector not in subs.keys():
                        subs[sector] = set()
                    
                    if not val in rows[r]:
                        rows[r].add(val)
                    else:
                        print('row collision', r, c, val, rows[r])
                        return False

                    if not val in cols[c]:
                        cols[c].add(val)
                    else:
                        print('col collision',  r, c, val)
                        return False
                    if not val in subs[sector]:
                        subs[sector].add(val)
                    else:
                        print('sector collision', r, c, val)
                        return False
        print(rows, cols, subs)
        return True