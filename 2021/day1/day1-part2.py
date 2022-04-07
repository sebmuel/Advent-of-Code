from readInput import read_input

# read content from file
content = read_input("input.txt", 'true')

totals = []

for index in range(len(content)):
    if (len(content) - index) > 3:
        sum = content[index] + content[index + 1] + content[index + 2]
        totals.append(sum)
       
j = 0
counter = 0

for i in totals:
    if i > j:
        counter += 1
    j = i   


print(counter)
