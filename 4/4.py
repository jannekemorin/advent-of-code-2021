from asyncio.windows_events import NULL

def read_lines():
    file = open('4\input.txt', 'r')
    return file.readlines() 

# Read in boards into this dataset
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
# } 
def get_boards(lines):
    boards = [[]]
    boards_dict = [{}]
    for line in lines[2:]:
        if line == "\n":
            boards.append([])
            boards_dict.append({})
        else: 
            boards[-1].append(line.split())
            for number in line.split():
                boards_dict[-1][number] = NULL
    return boards, boards_dict
# Example board:
# [
#     ['27', '71', '24', '3', '0'], 
#     ['79', '42', '32', '72', '62'], 
#     ['99', '52', '11', '92', '33'], 
#     ['38', '22', '16', '44', '39'], 
#     ['35', '26', '76', '49', '58']
# ]
# First, start with each number. Check if that number is in each board.
# Create another method that is called to check each board for Bingos 
# after checking each board for the number gathered above.
def check_number(number):
    return



# Main
lines = read_lines()
boards, boards_dict = get_boards(lines)
numbers = lines[0]