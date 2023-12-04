power, part1 = -1, 0
import numpy as np

game_cnt = 0

with open('input_2.txt') as f:
    lines = f.readlines()
    for game in lines:
        game_id = int(game.split(":")[0].split()[1]) 
        if game_id > game_cnt:
            game_cnt = game_id

    card_list = np.ones(game_cnt)
        
    for line in lines:
        numbers = line.split(":")
        index = int(numbers[0].split()[1]) - 1
        card = numbers[1].split("|")
        winning = card[0].split()
        my_nums = card[1].split()

        for num in my_nums:
            if num in winning:
                power += 1
        
        if power != -1:
            part1 += pow(2, power)
            tmp_index = index
            power += 1
            for scratchcards in range(power):
                card_list[tmp_index+1] += 1*card_list[index]
                tmp_index += 1
        power = -1
        
print("PART1:", part1)
print("PART2:", sum(card_list))