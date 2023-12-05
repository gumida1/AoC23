import re

key_dict, part1 = -2, 99999999999
seed_dict, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_ligth, light_to_temperature, temperature_to_humidity, humidity_to_location = {}, {}, {}, {}, {}, {}, {}, {}
maps_dict = {
    -1 : seed_dict,
    0 : seed_to_soil,
    1 : soil_to_fertilizer,
    2 : fertilizer_to_water,
    3 : water_to_ligth,
    4 : light_to_temperature,
    5 : temperature_to_humidity,
    6 : humidity_to_location
}
seeds = []

with open('input_2.txt') as f:
    lines = f.readlines()
    for line in lines:
        if re.search("seeds:", line):
            for num in line.split():
                if num.isnumeric(): seeds.append(int(num))
        words = line.split()
        
        if not words == [] and (re.search(":", words[1]) or re.search(":", words[0])): key_dict += 1
        elif not words == [] and re.search("\d+", words[0]):
            source = int(words[1])
            dest = int(words[0])
            for i in range(int(words[2])):
                cur_dict = maps_dict[key_dict]
                cur_dict[source] = dest
                source += 1
                dest += 1
                
    for seed in seeds:
        key_dict_2 = 0
        cur_seed = seed
        while key_dict_2 != 7:
            if cur_seed in maps_dict[key_dict_2]:
                cur_seed = maps_dict[key_dict_2][cur_seed]
            key_dict_2 += 1
        if cur_seed < part1 :
            part1 = cur_seed 
        
print(part1)