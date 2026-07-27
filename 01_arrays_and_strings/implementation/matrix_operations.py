"""
Matrix (2D Array) - Implement a 2D array with operations
Operations: insert(row, col, value), get(row, col), transpose(),
            rotate90(), spiralOrder()
"""


class Matrix:
    def __init__(self, row: int, col: int):
        self.matrix = [[0 for _ in range(col)] for _ in range(row)]
    
    def insert(self, row: int, col: int, value: int):
        if len(self.matrix) < row:
            raise IndexError("No Row available.")
        
        if len(self.matrix[row]) < col:
            raise IndexError("No Column available.")
        
        self.matrix[row][col] = value
        
    def get(self, row: int, col: int):
        if len(self.matrix) < row:
            raise IndexError("No Row available.")
        
        if len(self.matrix[row]) < col:
            raise IndexError("No Column available.")
        
        return self.matrix[row][col]
    
    def display(self):
        print(self.matrix)
    
    def transpose(self):
        trans_array = [[0 for _ in  range(len(self.matrix))] for _ in range(len(self.matrix[0]))]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                trans_array[j][i] = self.matrix[i][j]
                
        self.matrix = trans_array

    def rotate90(self, counterClockWise: bool = False):
        
        if not counterClockWise:
            self.transpose()
            for i in range(len(self.matrix)):
                self.matrix[i].reverse()
                
        else:
            self.transpose()
            self.matrix.reverse()
    
    def spiralOrder(self):
        max_raw = len(self.matrix) - 1
        max_col = len(self.matrix[0]) - 1
        
        start_raw = 0
        start_col = 0
        
        phase = 0
        
        raw = 0
        col = 0
        
        while True:
            
            print(self.matrix[raw][col], end=" -> ")
            
            if phase == 0:
                col += 1
                if col == max_col:
                    phase = 1
            elif phase == 1:
                raw += 1
                if raw == max_raw:
                    phase = 2
            elif phase == 2:
                col -= 1
                if col == start_col:
                    phase = 3
            elif phase == 3:
                raw -= 1
                if raw == start_raw:
                    phase = 0
                    
                    start_raw += 1
                    start_col += 1
                    
                    if start_raw == max_raw and start_col == max_col:
                        break
                    
                    max_raw -= 1
                    max_col -= 1
                    
                    raw = start_raw
                    col = start_col
        
    
if __name__ == "__main__":
    matrix = Matrix(4,4)    
    matrix.display()
    matrix.insert(0,0,1)
    matrix.insert(0,1,2)
    matrix.insert(0,2,3)
    matrix.insert(0,3,4)
    matrix.insert(1,0,5)
    matrix.insert(1,1,6)
    matrix.insert(1,2,7)
    matrix.insert(1,3,8)
    matrix.insert(2,0,9)
    matrix.insert(2,1,10)
    matrix.insert(2,2,11)
    matrix.insert(2,3,12)
    matrix.insert(3,0,13)
    matrix.insert(3,1,14)
    matrix.insert(3,2,15)
    matrix.insert(3,3,16)
    matrix.display()
    matrix.spiralOrder()
    # matrix.transpose()
    # matrix.display()
    # matrix.rotate90()
    # matrix.display()
    # matrix.rotate90(counterClockWise= True)
    # matrix.display()
    
