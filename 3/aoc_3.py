import numpy as np

rows, cols, index_r, index_c, cur_number, part1, first, second, part2 = 0, 0, -1, -1, 0, 0, 0, 0, 0
engine_part, three_numbers = False, False

def append_number(number, apendix):
    number = str(number) + str(apendix)
    return number 

def get_full_number(arr, r, c):
    value = arr[r][c]
    if arr[r][c+1].isnumeric():
        value = append_number(value, arr[r][c+1])
        if arr[r][c+2].isnumeric():
            value = append_number(value, arr[r][c+2])
    if arr[r][c-1].isnumeric():
        value = append_number(arr[r][c-1], value)
        if arr[r][c-2].isnumeric():
            value = append_number(arr[r][c-2], value)
    return int(value)

def save_two_numbers(num):
    global first, second
    if first == 0:
        first = num
    elif second == 0:
        if first != num:        #stejne cisla u hvezdicky to mrdaj
            second = num
    else:
        three_numbers = True
    
with open('input_2.txt') as f:
    lines = f.readlines()
    for line in lines:
        rows += 1
        cols = 0
        for c in line:
            cols += 1
        
    engine_arr = np.zeros((rows, cols), dtype='object')        
    for line in lines:
        index_r += 1
        for sym in line:
            index_c += 1
            if not sym == '\n': engine_arr[index_r][index_c] = sym
        index_c = -1        
        
    for row in range(rows):
        for col in range(cols):
            if engine_arr[row][col].isnumeric():
                cur_number = str(cur_number) + str(engine_arr[row][col])
                cur_number = int(cur_number)
                
                try:
                    if not(np.roll(engine_arr, 1)[row][col].isnumeric()) and np.roll(engine_arr, 1)[row][col] != '.' or not(np.roll(engine_arr, -1)[row][col].isnumeric()) and np.roll(engine_arr, -1)[row][col] != '.' or \
                                not(np.roll(engine_arr, 1, 0)[row][col].isnumeric()) and np.roll(engine_arr, 1, 0)[row][col] != '.' or not(np.roll(engine_arr, -1, 0)[row][col].isnumeric()) and np.roll(engine_arr, -1, 0)[row][col] != '.' or \
                                not(np.roll(engine_arr, -1, axis=(0, 1))[row][col].isnumeric()) and np.roll(engine_arr, -1, axis=(0, 1))[row][col] != '.' or not(np.roll(engine_arr, 1, axis=(0, 1))[row][col].isnumeric()) and np.roll(engine_arr, 1, axis=(0, 1))[row][col] != '.' or \
                                not(engine_arr[row+1][col-1].isnumeric()) and engine_arr[row+1][col-1] != '.' or not(engine_arr[row-1][col+1].isnumeric()) and engine_arr[row-1][col+1] != '.':                             #vylezani z pole to mrda
                        engine_part = True
                except:
                    pass
            else:
                if engine_part: 
                    part1 += cur_number

                cur_number = 0
                engine_part = False
            
            if engine_arr[row][col] == '*':
                if np.roll(engine_arr, 1)[row][col].isnumeric():
                    save_two_numbers(get_full_number(engine_arr, row, col-1))
                if np.roll(engine_arr, -1)[row][col].isnumeric():
                    save_two_numbers(get_full_number(engine_arr, row, col+1))
                if np.roll(engine_arr, 1, 0)[row][col].isnumeric():
                    save_two_numbers(get_full_number(engine_arr, row - 1, col))
                if np.roll(engine_arr, -1, 0)[row][col].isnumeric():
                    save_two_numbers(get_full_number(engine_arr, row + 1, col))
                if np.roll(engine_arr, -1, axis=(0, 1))[row][col].isnumeric():
                    save_two_numbers(get_full_number(engine_arr, row + 1, col + 1))
                if np.roll(engine_arr, 1, axis=(0, 1))[row][col].isnumeric():
                    save_two_numbers(get_full_number(engine_arr, row - 1, col - 1))
                if engine_arr[row+1][col-1].isnumeric():
                    save_two_numbers(get_full_number(engine_arr, row + 1, col - 1))
                if engine_arr[row-1][col+1].isnumeric():
                    save_two_numbers(get_full_number(engine_arr, row - 1, col + 1))
                
            if not three_numbers and first != 0 and second != 0:
                part2 += first * second

            first = 0
            second = 0
            three_numbers = False
            
    print("PART1:", part1)
    print("PART2:", part2)