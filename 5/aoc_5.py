import re
import multiprocessing
#from tqdm import tqdm

def for_partition(shared_part1, seed, seed2, lines):
    global part1
    cur_seed_part2 = seed2
    print("JSEM VE FCI PROCESU")
    for j in range(int(cur_seed_part2)):
        #print("[" + str(j) + str(range(int(cur_seed_part2))) + "]")
        cur_seed = seed + j
        i = 0
        for line in lines:
            words = line.split()

            if not words == [] and (re.search(":", words[1]) or re.search(":", words[0])):
                not_found_yet = True
            if not words == [] and re.search("\d+", words[0]):
                if cur_seed >= int(words[1]) and cur_seed < int(words[1]) + int(words[2]) and not_found_yet:
                    cur_seed = cur_seed - int(words[1]) + int(words[0])
                    not_found_yet = False
            if cur_seed < shared_part1.value and i == len(lines) - 1:
                shared_part1.value = cur_seed
                print("NOVA NEJNIZSI HODNOTA: ", shared_part1.value)
            i += 1
    print("FUNKCE PROCESU DONE")

if __name__ == "__main__":
    with open('input_2.txt') as f:
        lines = f.readlines()

        manager = multiprocessing.Manager()
        part1 = manager.Value('i', 4288015284)

        seeds = []
        part2_seeds = []
        location = False
        not_found_yet = True
        beg = True
        processes = []

        for line in lines:
            if re.search("seeds:", line):
                for num in line.split():
                    if num.isdigit():
                        seeds.append(int(num))

        for seed in seeds:
            if beg:
                seed1 = seed
                beg = False
            else:
                print("NEW PROCES")
                p = multiprocessing.Process(target=for_partition, args=(part1, seed1, seed, lines))
                processes.append(p)
                p.start()
                beg = True

        for process in processes:
            process.join()
            print("JOIN")

        print("PART1:", part1.value)