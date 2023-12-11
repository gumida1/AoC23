#potreba odtrackovat output kde nastane chyba 

import numpy as np

go_right = ('-', 'J', '7')
go_left = ('-', 'L', 'F')
go_top = ('|', 'F', '7')
go_bot = ('|', 'L', 'J')

r_index, c_index, cur_pipe, pipe_cnt = -1, -1, 's', 0

with open('input_2.txt') as f:
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
            
        print(cur_pipe, ex_pipe)
    
    print(pipes_map)
    print(starting_point)
    print(pipe_cnt/2)