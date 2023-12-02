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

def findFirstDigit(sentence):
    for ch in sentence:
        if ch.isdigit():
            return ch

def main():
    input = open("input.txt", "r")
    input_lines = input.readlines()

    part_one = part_two = 0

    for line in input_lines:
        first = findFirstDigit(line)
        last = findFirstDigit(line[::-1])
        part_one += int(str(first)+str(last))

        identifiedNumbersLine = identifyStringNumbers(line)
        first = findFirstDigit(identifiedNumbersLine)
        last = findFirstDigit(identifiedNumbersLine[::-1])
        part_two += int(str(first)+str(last))       

    print('part_one', part_one)
    print('part_one', part_two)

if __name__ == "__main__":
    main()