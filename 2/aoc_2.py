import re
r_max, g_max, b_max, part1, part2 = 0, 0, 0, 0, 0
turn = True

with open('input_2.txt') as f:
    lines = f.readlines()
    for line in lines:
        gameid = line.split(": ")[0][5:]
        color_list = re.split(',|:|;', line)
        for color in color_list:
            color_count = color.split()
            if color_count[1] == "red" and int(color_count[0]) <= 12 or color_count[1] == "green" and int(color_count[0]) <= 13 or color_count[1] == "blue" and int(color_count[0]) <= 14:
                turn = True
            else:
                turn = False
                if color_count[0] != "Game":
                    break
                
        for color2 in color_list:
            color_count2 = color2.split()
            if color_count2[1] == "red" and int(color_count2[0]) > r_max:
                r_max = int(color_count2[0])
            elif color_count2[1] == "green" and int(color_count2[0]) > g_max:
                g_max = int(color_count2[0])
            elif color_count2[1] == "blue" and int(color_count2[0]) > b_max:
                b_max = int(color_count2[0])
                
        part2 += r_max * g_max * b_max
        r_max, g_max, b_max = 0, 0, 0      
         
        if turn == True:
            part1 += int(gameid)
        turn = True

print(part1)
print(part2)        