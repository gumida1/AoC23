import numpy as np

go_right = ('-', 'J', '7')
go_left = ('-', 'L', 'F')
go_top = ('|', 'F', '7')
go_bot = ('|', 'L', 'J')

r_index, c_index, cur_pipe, pipe_cnt, tiles_in_loop = -1, -1, 's', 0, 0
pipe_border = []
is_in = False 

with open('input_0.txt') as f:
    lines = f.readlines()
    pipes_map = np.zeros((len(lines), len(lines[0]) - 1), dtype='object')
    for line in lines:
        r_index += 1
        for c in line:
            c_index += 1        
            if c != '\n': pipes_map[r_index][c_index] = c
            if c == 'S': starting_point = (r_index, c_index)
        c_index = -1
        
    while cur_pipe != 'S':                  #while na cely pipe loop
        if cur_pipe == 's':                 #starting point
            if pipes_map[starting_point[0]][starting_point[1] + 1] in go_right:
                cur_pipe = pipes_map[starting_point[0]][starting_point[1] + 1]
                starting_point = (starting_point[0], starting_point[1] + 1)
                ex_pipe = 'L'
                from_right = False
            elif pipes_map[starting_point[0]][starting_point[1] - 1] in go_left:
                cur_pipe = pipes_map[starting_point[0]][starting_point[1] - 1]
                starting_point = (starting_point[0], starting_point[1] - 1)
                ex_pipe = 'J'
                from_right = True
            elif pipes_map[starting_point[0] + 1][starting_point[1]] in go_bot:
                cur_pipe = pipes_map[starting_point[0] + 1][starting_point[1]]
                starting_point = (starting_point[0] + 1, starting_point[1])
                ex_pipe = '7'
                from_bot = False
            elif pipes_map[starting_point[0] - 1][starting_point[1]] in go_top:
                cur_pipe = pipes_map[starting_point[0] - 1][starting_point[1]]
                starting_point = (starting_point[0] - 1, starting_point[1])
                ex_pipe = 'L'
                from_bot = True
            pipe_cnt += 1
        
        elif cur_pipe == '-':
            if ex_pipe in go_right:
                if ex_pipe == '-' and not from_right:
                    ex_pipe = cur_pipe
                    cur_pipe = pipes_map[starting_point[0]][starting_point[1] + 1]
                    starting_point = (starting_point[0], starting_point[1] + 1)
                    from_right = False
                else:
                    ex_pipe = cur_pipe
                    cur_pipe = pipes_map[starting_point[0]][starting_point[1] - 1]
                    starting_point = (starting_point[0], starting_point[1] - 1)
                    from_right = True
            else:
                ex_pipe = cur_pipe
                cur_pipe = pipes_map[starting_point[0]][starting_point[1] + 1]
                starting_point = (starting_point[0], starting_point[1] + 1)
                from_right = False
            pipe_cnt += 1
            
        elif cur_pipe == '7':
            if ex_pipe in go_bot:
                if ex_pipe == 'L' and not from_right:
                    ex_pipe = cur_pipe
                    cur_pipe = pipes_map[starting_point[0] + 1][starting_point[1]]
                    starting_point = (starting_point[0] + 1, starting_point[1])
                    from_bot = False
                else:
                    ex_pipe = cur_pipe
                    cur_pipe = pipes_map[starting_point[0]][starting_point[1] - 1]
                    starting_point = (starting_point[0], starting_point[1] - 1)
                    from_right = True
            else:
                ex_pipe = cur_pipe
                cur_pipe = pipes_map[starting_point[0] + 1][starting_point[1]]
                starting_point = (starting_point[0] + 1, starting_point[1])
                from_bot = False
            pipe_cnt += 1
        
        elif cur_pipe == '|':
            if ex_pipe in go_bot:
                if ex_pipe == '|' and not from_bot:
                    ex_pipe = cur_pipe
                    cur_pipe = pipes_map[starting_point[0] + 1][starting_point[1]]
                    starting_point = (starting_point[0] + 1, starting_point[1])
                    from_bot = False
                else:
                    ex_pipe = cur_pipe
                    cur_pipe = pipes_map[starting_point[0] - 1][starting_point[1]]
                    starting_point = (starting_point[0] - 1, starting_point[1])
                    from_bot = True
            else:
                ex_pipe = cur_pipe
                cur_pipe = pipes_map[starting_point[0] + 1][starting_point[1]]
                starting_point = (starting_point[0] + 1, starting_point[1])
                from_bot = False
            pipe_cnt += 1
        
        elif cur_pipe == 'J':
            if ex_pipe in go_top:
                if ex_pipe == 'F' and not from_right:
                    ex_pipe = cur_pipe
                    cur_pipe = pipes_map[starting_point[0] - 1][starting_point[1]]
                    starting_point = (starting_point[0] - 1, starting_point[1])
                    from_bot = True
                else:
                    ex_pipe = cur_pipe
                    cur_pipe = pipes_map[starting_point[0]][starting_point[1] - 1]
                    starting_point = (starting_point[0], starting_point[1] - 1)
                    from_right = True
            else:
                ex_pipe = cur_pipe
                cur_pipe = pipes_map[starting_point[0] - 1][starting_point[1]]
                starting_point = (starting_point[0] - 1, starting_point[1])
                from_bot = True
            pipe_cnt += 1
            
        elif cur_pipe == 'L':
            if ex_pipe in go_top:
                if ex_pipe == '7' and from_right:
                    ex_pipe = cur_pipe
                    cur_pipe = pipes_map[starting_point[0] - 1][starting_point[1]]
                    starting_point = (starting_point[0] - 1, starting_point[1])
                    from_bot = True
                else:
                    ex_pipe = cur_pipe
                    cur_pipe = pipes_map[starting_point[0]][starting_point[1] + 1]
                    starting_point = (starting_point[0], starting_point[1] + 1)
                    from_right = False
            else:
                ex_pipe = cur_pipe
                cur_pipe = pipes_map[starting_point[0] - 1][starting_point[1]]
                starting_point = (starting_point[0] - 1, starting_point[1])
                from_bot = True
            pipe_cnt += 1
        
        elif cur_pipe == 'F':
            if ex_pipe in go_bot:
                if ex_pipe == 'J' and from_right:
                    ex_pipe = cur_pipe
                    cur_pipe = pipes_map[starting_point[0] + 1][starting_point[1]]
                    starting_point = (starting_point[0] + 1, starting_point[1])
                    from_bot = False
                else:
                    ex_pipe = cur_pipe
                    cur_pipe = pipes_map[starting_point[0]][starting_point[1] + 1]
                    starting_point = (starting_point[0], starting_point[1] + 1)
                    from_right = False
            else:
                ex_pipe = cur_pipe
                cur_pipe = pipes_map[starting_point[0] + 1][starting_point[1]]
                starting_point = (starting_point[0] + 1, starting_point[1])
                from_bot = False
            pipe_cnt += 1
        
        pipe_border.append((starting_point[0], starting_point[1]))
        print(cur_pipe, starting_point[0], starting_point[1])

    for row in range(len(lines)):
        for col in range(len(lines[0]) - 1):
            print(row, col)
            if (row, col) in pipe_border:
                print("xd")
            if (row, col - 1) in pipe_border:
                is_in = not is_in
                print("toggled in", is_in, row, col)
            elif (row, col - 1) not in pipe_border:
                is_in = not is_in
                print("toggled in", is_in, row, col)
        
            if is_in:
                tiles_in_loop += 1
                print(is_in, (row, col), tiles_in_loop)
        is_in = False
            
    print(pipe_border, len(pipe_border))    
    print("PART 1:", pipe_cnt/2)
    print("PART 2:", tiles_in_loop)
    print((len(lines), len(lines[0]) - 1))
