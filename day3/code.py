def check_adjacent(grid, row, cols):
    cols = cols.split(',')[:-1]
    prev_row = row - 1
    next_row = row + 1

    if prev_row >= 0:
        for col in range(int(cols[0]) - 1, int(cols[-1]) + 2):
            if col >= 0 and col < len(grid[prev_row]):
                if not grid[prev_row][col].isdigit() and grid[prev_row][col] != '.':
                    return True

    if next_row < len(grid):
        for col in range(int(cols[0]) - 1, int(cols[-1]) + 2):
            if col >= 0 and col < len(grid[next_row]):
                if not grid[next_row][col].isdigit() and grid[next_row][col] != '.':
                    return True  # Changed from False to True

    if (grid[row][int(cols[0]) - 1] != '.' and not grid[row][int(cols[0]) - 1].isdigit()) or (grid[row][int(cols[-1]) + 1] != '.' and not grid[row][int(cols[-1]) + 1].isdigit()):
        return True
    

def part_numbers(grid):
    s = 0
    for i in range(len(grid)):
        row = grid[i]
        number = ''
        index = ''
        for j in range(len(row)):
            element = row[j]
            if element.isdigit():
                number += element
                index += str(j) + ','
            else:
                if number != '' and check_adjacent(grid, i, index):
                    s += int(number)
                number = ''
                index = ''
    print(s)                

def main():
    input = open("input.txt", "r")
    input_lines = input.readlines()

    grid = []
    for line in input_lines:
        line = line.rstrip()
        row = []
        for char in line:
            row.append(char)
        grid.append(row)

    part_numbers(grid)

if __name__ == "__main__":
    main()
