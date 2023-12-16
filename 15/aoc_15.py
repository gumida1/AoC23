part1 = 0
with open('input_2.txt') as f:
    lines = f.readlines()
    seq = lines[0].split(',')
    for s in seq:
        code, current_val = s, 0
        for char in s:
            current_val = ((current_val + ord(char)) * 17) % 256
        part1 += current_val
    print("PART 1:",part1)