file = open('depths.txt', 'r')
lines = file.readlines()

def part_1():
    num_depth_increases = 0
    for i in range(1, len(lines)):
        #print((str(i) + ", " + str(lines[i]).strip() + " > " + str(lines[i-1])).strip() + " " + str(lines[i] > lines[i-1]))
        if lines[i] > lines[i-1]:
            num_depth_increases += 1

    return num_depth_increases

def part_2():
    num_sum_increases = 0
    for i in range(len(lines)-2):
        sum = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
        if (i > 0) and (sum > prev_sum):
            num_sum_increases += 1
        prev_sum = sum
    
    return num_sum_increases

print("Part 1: " + str(part_1()))
print("Part 2: " + str(part_2()))
