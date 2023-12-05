import re

key_dict, part1 = -2, 4288015284
first_dict = {}
seeds = []

with open('input_2.txt') as f:
    lines = f.readlines()
    for line in lines:
        if re.search("seeds:", line):
            for num in line.split():
                if num.isnumeric(): seeds.append(int(num))                  #prirazene seedy do pole seeds[]
        else:
            words = line.split()            #rozdeleni po mezerach
            
            if not words == [] and (re.search(":", words[1]) or re.search(":", words[0])):      #hledam prazdny radek a radek s dvojteckou
                
                if not first_dict == {}:        #kontrola jestli je first dict jiz zaplneny alespon prvni varkou
                    new_seeds = seeds
                    seeds = []
                    
                    for seed in new_seeds:          #prochazeni seminek 
                        cur_seed = seed
                        if cur_seed in first_dict:      #pokud je seminko ve slovniku -> zmenim ho na namapovane
                            cur_seed = first_dict[cur_seed]
                        seeds.append(cur_seed)          #do vycistenych seminek vkladam nove zjistene
                
                first_dict = {}         #vycisteni slovniku
            
            elif not words == [] and re.search("\d+", words[0]):        #hledam mapujici cisla a ukladam do slovniku
                source = int(words[1])
                dest = int(words[0])
                for i in range(int(words[2])):
                    first_dict[source] = dest
                    source += 1
                    dest += 1
       
print(min(seeds))
