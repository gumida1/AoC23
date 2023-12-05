import re

key_dict, part1 = -2, 4288015284
first_dict = {}
seeds = []
location, not_found_yet = False, True

with open('input_2.txt') as f:
    lines = f.readlines()
    for line in lines:
        if re.search("seeds:", line):
            for num in line.split():
                if num.isnumeric(): seeds.append(int(num))                  #prirazene seedy do pole seeds[]

    for seed in seeds:
        cur_seed = seed
        i = 0
        for line in lines:
            words = line.split()    
            
            if not words == [] and (re.search(":", words[1]) or re.search(":", words[0])):      #hledam prazdny radek a radek s dvojteckou
                not_found_yet = True       
            if not words == [] and re.search("\d+", words[0]):        
                if cur_seed >= int(words[1]) and cur_seed < int(words[1]) + int(words[2]) and not_found_yet:
                    cur_seed = cur_seed - int(words[1]) + int(words[0])
                    not_found_yet = False
            if cur_seed < part1 and i == len(lines) - 1:
                part1 = cur_seed
                location = False
            i += 1
        
print("PART1:", part1)