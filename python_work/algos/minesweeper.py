"""

Write a function that will take in 3 arguments: 
bombs = list of bomb locations 
rows, columns

mine_sweeper([[0,0], [1,2]], 3, 4)

bombs at row index 0 column index 0 
bombs at row index 0 column index 1
3 rows 
3 columns

we should return an 3 x 4 array (-1) = bomb
"""

def mine_sweeper(bombs, num_rows, num_cols): 
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]

    for bomb_location in bombs: 
        (bomb_row, bomb_col) = bomb_location
        field[bomb_row][bomb_col] = -1

        row_range = range(bomb_row - 1, bomb_row + 2)
        col_range = range(bomb_col - 1, bomb_col + 2)

        for i in row_range: 
            current_i = i 
            for j in col_range: 
                current_j = j 
                if(0 <= i < num_rows and 0 <= j < num_cols and field[i][j] != -1):
                    field[i][j] += 1

    print(field) 

mine_sweeper([[0,0], [1,2]], 3, 4)