input = open("input.txt", "r")

input_lines = input.readlines()

word_to_number = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def identifyStringNumbers(string):
    result = ''
    length = len(string)
    start = 0

    while start < length:
        if string[start].isdigit():
            result += string[start]
            start += 1
        else:
            for end in range(start + 1, length + 1):
                current_word = string[start:end]
                if current_word.lower() in word_to_number:
                    result += str(word_to_number[current_word.lower()])
                    start = end
                    break
            else:
                # If no valid word is found, increment the counter
                result += string[start]
                start += 1

    return result



sum = 0

for line in input_lines:
    # print(line)
    first = last = -1
    line = identifyStringNumbers(line)
    # print(line)
    for element in range(0, len(line)):
        if(line[element].isdigit()):
            # print('first digit is', i[element])
            first = line[element]
            break
    for element in range(len(line)-1, -1, -1):
        if(line[element].isdigit()):
            # print('last digit is', i[element])
            last = line[element]
            break
    if(first == -1 or last == -1):
        print(first, last)
    # print('number is ', str(first)+str(last))
    # print()
    sum += int(str(first)+str(last))

print('sum is', sum)
