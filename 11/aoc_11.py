import numpy as np

rows, cols, r_index, c_index, galaxy_cnt, part1, part2, empty_r, empty_c = 0, 0, -1, -1, 0, 0, 0, 0, 0
galaxy_found = False
no_galaxies_rows, no_galaxies_cols  = [], []
galaxies_dict = {}

with open('input_2.txt') as f:
    lines = f.readlines()
    for line in lines:
        rows += 1
        cols = 0
        for c in line:
            if c == '#': 
                galaxy_found = True
                galaxy_cnt += 1
                galaxies_dict[galaxy_cnt] = (rows-1, cols)
            cols += 1
        if not galaxy_found: no_galaxies_rows.append(rows - 1) 
        galaxy_found = False
            
    galaxy_grid_np = np.zeros((rows, cols), dtype='object')
    for line in lines:
        r_index += 1
        for c in line:
            c_index += 1        
            if c != '\n': galaxy_grid_np[r_index][c_index] = c
        c_index = -1
    
    galaxy_found = False
    for col in range(cols):
        for row in range(rows):
            if galaxy_grid_np[row][col] == '#': galaxy_found = True
        if not galaxy_found: no_galaxies_cols.append(col)
        galaxy_found = False

    for src in galaxies_dict:
        for dest in galaxies_dict:
            if dest > src:
                lower, higher = min(galaxies_dict[src][1], galaxies_dict[dest][1]), max(galaxies_dict[src][1], galaxies_dict[dest][1])                
                for empty_row in no_galaxies_rows:
                    if galaxies_dict[dest][0] > empty_row and galaxies_dict[src][0] < empty_row: empty_r += 1
                for empty_col in no_galaxies_cols:
                    if higher > empty_col and lower < empty_col: empty_c += 1
                    
                part1 += (galaxies_dict[dest][0] - galaxies_dict[src][0]) + (higher - lower) + empty_r + empty_c
                part2 += (galaxies_dict[dest][0] - galaxies_dict[src][0]) + (higher - lower) + (empty_r*999999) + (empty_c*999999)
                empty_r, empty_c = 0, 0

print("PART 1:", part1)
print("PART 2:", part2)