import re
import math

directions = {}
total_steps, total_steps2 = 0, 0
total_steps_arr = []
end = False
with open('input_2.txt') as f:
    lines = f.readlines()
    for line in lines:
        splitted = line.split()
        if len(splitted) > 1 and splitted[1] == "=":
            directions[splitted[0]] = [splitted[2].replace("(", "").replace(",", ""), splitted[3].replace(")", "")]
    
    cur_location = "AAA"
    while not end:
        for lr in lines[0]:
            if lr == "L":
                cur_location = directions[cur_location][0]
                total_steps += 1                
            elif lr == "R":
                cur_location = directions[cur_location][1]
                total_steps += 1
            
            if cur_location == "ZZZ":
                end = True    
    
    ## PART 2 
    ghost_numbers, tmp = {}, {}
    cur_location2 = ""
    for dirs in directions:
        if re.search("A$", dirs):
            ghost_numbers[dirs] = directions[dirs]
    
    for ghost in ghost_numbers:
        end = False
        while not end:
            for lr in lines[0]:
                if lr == "L":
                    ghost = directions[ghost][0]
                    total_steps2 += 1
                elif lr == "R":
                    ghost = directions[ghost][1]
                    total_steps2 += 1
                if re.search("Z$", ghost):
                    total_steps_arr.append(total_steps2)
                    end = True
                    total_steps2 = 0
                    break
    
    print("PART1:", total_steps)                
    print("PART2:", math.lcm(total_steps_arr[0], total_steps_arr[1], total_steps_arr[2], total_steps_arr[3], total_steps_arr[4], total_steps_arr[5])) 
    