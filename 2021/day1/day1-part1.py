
with open('input.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    
input = []
j = 0
counter = 0

for line in lines:
    input.append(int(line))
    
for i in input:
    if i > j:
        counter += 1
    j = i    

print(counter-1)
        
    
    