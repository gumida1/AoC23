part1, part2 = 0, 0
with open('input_2.txt') as f:
    lines = f.readlines()
    for line in lines:
        end = False
        tmp, last_values, first_values = [], [], []
        splitted = line.split()
        last_values.append(int(splitted[-1]))
        first_values.append(int(splitted[0]))
        while not end:
            tmp = []
            for i in range(len(splitted)):
                if not i == len(splitted)-1 :
                    new_value = int(splitted[i+1]) - int(splitted[i])
                    tmp.append(new_value)
            last_values.append(tmp[-1])
            first_values.append(tmp[0])
            splitted = tmp
            
            if all(v == 0 for v in splitted):
                part1 += sum(last_values)
                tmp_val = 0    
                for i in range(len(first_values)):
                    tmp_val = first_values[-i-1] - tmp_val    
                part2 += tmp_val
                end = True
                    
print("PART1:", part1)
print("PART2:", part2)