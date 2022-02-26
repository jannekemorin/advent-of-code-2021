file = open('4\input.txt', 'r')
lines = file.readlines() 

numbers = lines[0]

print(numbers)

# Read in boards
b = []
for row in lines[1:]:
    if row == "\n":
        b.append([])
        for i in range(4):
            

            
