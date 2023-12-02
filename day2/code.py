# part_one
# step 1: split : then first part contains id, and second contains game draws
# step 2: split ; and then for each item split on white space, use the second element to check the bag dict,
# step 3: see if the number is less than or eq than bag allowed, if all g, add bag id 

# part_two
# from step 2, find max of each cube req for a game
# multiple the max together

def extractGameIDContent(game):
    return game.split(': ')

def isValidGame(game_content, bag):
    for game in game_content.split('; '):
        for cube in game.split(", "):
            count, color = cube.split(' ')
            count = int(count)
            color = color.lower()

            if count > int(bag[color]):
                return False
    return True


def calcPower(gameContent):
    max_values = {'red': -1, 'green': -1, 'blue': -1}

    gameDraws = gameContent.split('; ')
    for game in gameDraws:
        cubes = game.split(", ")
        for cube in cubes:
            count, color = cube.split(' ')
            count = int(count)
            
            if count > max_values[color]:
                max_values[color] = count

    return max_values['red'] * max_values['green'] * max_values['blue']

def main():
    input = open("input.txt", "r")
    input_lines = input.readlines()

    bag = {'red':12, 'green': 13, 'blue': 14}

    part_one = part_two = 0

    for line in input_lines:
        gameID, gameContent = extractGameIDContent(line.rstrip())
        gameID = int(gameID.split(" ")[1])
        if isValidGame(gameContent, bag):
            part_one += gameID
        part_two += calcPower(gameContent)

    print('part_one', part_one)
    print('part_one', part_two)

if __name__ == "__main__":
    main()