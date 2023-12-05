import input

inputText = input.input

inputText = inputText.replace("one", "o1e")
inputText = inputText.replace("two", "t2o")
inputText = inputText.replace("three", "t3e")
inputText = inputText.replace("four", "f4r")
inputText = inputText.replace("five", "f5e")
inputText = inputText.replace("six", "s6x")
inputText = inputText.replace("seven", "s7n")
inputText = inputText.replace("eight", "e8t")
inputText = inputText.replace("nine", "n9e")
inputText = inputText.replace("zero", "z0o")

#1.1
sum = 0
for line in inputText.split('\n'):
    first = "0"
    last = "0"
    for char in line:
        if(char.isdigit()):
            if(first == "0"):
                first = char
                last = char
            else:
                last = char
    print(first+last)
    sum += int(first+last)

print("1.2: ", sum)
