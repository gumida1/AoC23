import re

key_dict, part1 = -2, 4288015284
seed_dict, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_ligth, light_to_temperature, temperature_to_humidity, humidity_to_location = {}, {}, {}, {}, {}, {}, {}, {}
"""maps_dict = {
    -1 : seed_dict,
    0 : seed_to_soil,
    1 : soil_to_fertilizer,
    2 : fertilizer_to_water,
    3 : water_to_ligth,
    4 : light_to_temperature,
    5 : temperature_to_humidity,
    6 : humidity_to_location
}"""
seeds = []

#maxim = 0
with open('input_2.txt') as f:
    lines = f.readlines()
    for line in lines:
        if re.search("seeds:", line):
            for num in line.split():
                if num.isnumeric(): seeds.append(int(num))
        words = line.split()
        """for word in words:
            if word.isnumeric() and int(word) > maxim:
                maxim = int(word)"""
        if not words == [] and (re.search(":", words[1]) or re.search(":", words[0])): key_dict += 1
        elif not words == [] and re.search("\d+", words[0]):
            source = int(words[1])
            dest = int(words[0])
            for i in range(int(words[2])):
                if key_dict == -1:
                    seed_dict[source] = dest
                    source += 1
                    dest += 1
                elif key_dict == 0:
                    seed_to_soil[source] = dest
                    source += 1
                    dest += 1
                elif key_dict == 1:
                    soil_to_fertilizer[source] = dest
                    source += 1
                    dest += 1
                elif key_dict == 2:
                    fertilizer_to_water[source] = dest
                    source += 1
                    dest += 1
                elif key_dict == 3:
                    water_to_ligth[source] = dest
                    source += 1
                    dest += 1
                elif key_dict == 4:
                    light_to_temperature[source] = dest
                    source += 1
                    dest += 1
                elif key_dict == 5:
                    temperature_to_humidity[source] = dest
                    source += 1
                    dest += 1
                elif key_dict == 6:
                    humidity_to_location[source] = dest
                    source += 1
                    dest += 1
                
    for seed in seeds:
        key_dict_2 = 0
        cur_seed = seed
        while key_dict_2 != 7:
            if key_dict_2 == 0:
                if cur_seed in seed_to_soil:
                    cur_seed = seed_to_soil[cur_seed]
                key_dict_2 += 1
            elif key_dict_2 == 1:
                if cur_seed in soil_to_fertilizer:
                    cur_seed = soil_to_fertilizer[cur_seed]
                key_dict_2 += 1
            elif key_dict_2 == 2:
                if cur_seed in fertilizer_to_water:
                    cur_seed = fertilizer_to_water[cur_seed]
                key_dict_2 += 1
            elif key_dict_2 == 3:
                if cur_seed in water_to_ligth:
                    cur_seed = water_to_ligth[cur_seed]
                key_dict_2 += 1
            elif key_dict_2 == 4:
                if cur_seed in light_to_temperature:
                    cur_seed = light_to_temperature[cur_seed]
                key_dict_2 += 1
            elif key_dict_2 == 5:
                if cur_seed in temperature_to_humidity:
                    cur_seed = temperature_to_humidity[cur_seed]
                key_dict_2 += 1
            elif key_dict_2 == 6:
                if cur_seed in humidity_to_location:
                    cur_seed = humidity_to_location[cur_seed]
                key_dict_2 += 1
            
        if cur_seed < part1 :
            part1 = cur_seed 
        
print(part1)