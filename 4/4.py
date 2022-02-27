import math

'''Helper functions'''
# Read in lines
def read_lines():
    file = open('4\input.txt', 'r')
    return file.readlines() 

# Read in boards into this dataset, creating a dictionary of numbers in the board for each board
# [                              <- This is the datastructure to hold the boards
#  [                             <- This is the first board
#     [], [], [], [], [], []..., <- This is one row
#     [], [], [], [], [], []..., <- This is one row
#     [], [], [], [], [], []...  <- This is one row
#  ],
#  [                             <- This is the second board
#     [], [], [], [], [], []..., <- This is one row
#     [], [], [], [], [], []..., <- This is one row
#     [], [], [], [], [], []...  <- This is one row
#  ]
# Example board:
# [
#     ['27', '71', '24', '3', '0'], 
#     ['79', '42', '32', '72', '62'], 
#     ['99', '52', '11', '92', '33'], 
#     ['38', '22', '16', '44', '39'], 
#     ['35', '26', '76', '49', '58']
# ]
def get_boards(lines):
    index = 0
    boards = [[]]
    boards_dict = [{}]
    for line in lines[2:]:
        if line == "\n":
            boards.append([])
            boards_dict.append({})
            index = 0
        else: 
            boards[-1].append(line.split())
            for number in line.split():
                boards_dict[-1][number] = index
                index += 1
    return boards, boards_dict

# Check whether a number is in each board. If it is, mark it with an 'X'
def check_number(boards, boards_dict, number):
    num_boards = len(boards)
    for i in range(num_boards):
        if number in boards_dict[i]:
            index = boards_dict[i].get(number)
            row = math.floor(index / 5)
            boards[i][row][index % 5] = 'X'
            
# Check whether there are any rows or columns with all Xs...return the index of the board with bingo if found
def check_for_bingo(boards):
    bingo = False
    num_boards = len(boards)
    i = 0
    while not bingo and i < num_boards:
        # Check rows
        for row in boards[i]:
            count = 0
            for item in row:
                if item == 'X':
                    count += 1
                if count == 5:
                    bingo = True
        # Check columns
        for j in range(5):
            count = 0
            for row in boards[i]:
                if row[j] == 'X':
                    count += 1
                if count == 5:
                    bingo = True
        i += 1
    return bingo, i

# Get the sum of all unmarked elements on a board
def count_unmarked(board, index):
    count = 0
    for row in board[index]:
        for item in row:
            if item != 'X':
                count += int(item)
    return count


'''Main function'''
lines = read_lines()
boards, boards_dict = get_boards(lines)
numbers = lines[0]
bingo = False
# For each number in the call list, mark up the boards that contain that number, then check for bingos
for number in numbers.split(','):
    check_number(boards, boards_dict, number)
    bingo, index = check_for_bingo(boards)
    if bingo:
        break
# Print the last number called X the sum of unmarked numbers on the winning board
print(int(number) * count_unmarked(boards, index-1))