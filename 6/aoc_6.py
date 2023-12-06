my_time, part1_2, beated = 0, 1, 0
t_d_dict = {}
big_time, big_dist = "", ""
part_2 = True

with open('input_2.txt') as f:
    lines = f.readlines()
    times = lines[0][5:].split()
    dist = lines[1][9:].split()
    if part_2:
        for time in times:
            big_time = big_time + time
        big_time = int(big_time)
        for dis in dist:
            big_dist = big_dist + dis
        big_dist = int(big_dist)
        times = big_time
        dist = big_dist   
        print(times, dist) 
    try:
        for i in range(len(times)):
            t_d_dict[times[i]] = dist[i]
    except:
        t_d_dict[times] = dist
        
    for x in t_d_dict:
        while my_time != int(x):
            my_dist = my_time * (int(x) - int(my_time))
            if my_dist > int(t_d_dict[x]):
                beated += 1
            my_time += 1
                
        part1_2 = part1_2 * beated
        beated, my_time = 0, 0
        
print(part1_2)