file = open('data.txt', 'r')
lines = file.readlines() 
lines = [str(line.strip()) for line in lines]

# Helper function --- retrieved from: https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/
def b2d(binary):
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def part_1():
    gamma = " "
    epsilon = " "
    tally_0 = 0
    tally_1 = 0
    binary_len = len(lines[0].strip())
    for i in range(binary_len):
        tally_0 = 0
        tally_1 = 0
        for line in lines:
            if line[i] == "0":
                tally_0 += 1
            elif line[i] == "1":
                tally_1 += 1
        if tally_0 > tally_1:
            gamma += "0"
            epsilon += "1"
        elif tally_1 > tally_0:
            gamma += "1"
            epsilon += "0"
    return(b2d(int(epsilon)) * b2d(int(gamma)))

def part_2():
    oxygen_generator_rating = lines.copy()
    co2_scrubber_rating = lines.copy()
    binary_len = len(lines[0])
    for i in range(binary_len):
        # Oxygen generator rating
        tally_0 = 0
        tally_1 = 0
        for line in oxygen_generator_rating:
            if line[i] == "0":
                tally_0 += 1
            elif line[i] == "1":
                tally_1 += 1
        copy = oxygen_generator_rating.copy()
        if(len(copy) == 1): 
            break
        elif tally_1 > tally_0:
            for line in oxygen_generator_rating:
                if line[i] == "0":
                    copy.remove(line)
        elif tally_0 > tally_1:
            for line in oxygen_generator_rating:
                if line[i] == "1":
                    copy.remove(line)
        else:
            for line in oxygen_generator_rating:
                if line[i] == "0":
                    copy.remove(line)
        oxygen_generator_rating = copy

        # cO2 scrubber rating
        tally_0 = 0
        tally_1 = 0
        for line in co2_scrubber_rating:
            if line[i] == "0":
                tally_0 += 1
            elif line[i] == "1":
                tally_1 += 1
        copy = co2_scrubber_rating.copy()
        if(len(copy) == 1): 
            copy = copy
        elif tally_1 > tally_0:
            for line in co2_scrubber_rating:
                if line[i] == "1":
                    copy.remove(line)
        elif tally_0 > tally_1:
            for line in co2_scrubber_rating:
                if line[i] == "0":
                    copy.remove(line)
        else:
            for line in co2_scrubber_rating:
                if line[i] == "1":
                    copy.remove(line)
        co2_scrubber_rating = copy
    return str(b2d(int(oxygen_generator_rating[0]))*b2d(int(co2_scrubber_rating[0])))


print("Part 1: " + str(part_1()))
print("Part 2: " + str(part_2()))

