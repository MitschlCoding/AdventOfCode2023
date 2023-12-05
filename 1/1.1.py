import input

#1.1
sum = 0
for line in input.input.split('\n'):
    first = "0"
    last = "0"
    for char in line:
        if(char.isdigit()):
            if(first == "0"):
                first = char
                last = char
            else:
                last = char
    sum += int(first+last)

print("1.1: ", sum)
