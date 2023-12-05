import input

"""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

string = input.input

redMax = 12
greenMax = 13
blueMax = 14


games = string.split('\n')

def gameIsPossible(game):
    game = game.split(':')[1]
    game = game.split(';')
    for round in game:
        round = round.split(',')
        for color in round:
            color = color.strip()
            color = color.split(' ')
            if(color[1] == 'red'):
                red = int(color[0])
                if(red > redMax):
                    return False
            elif(color[1] == 'green'):
                green = int(color[0])
                if(green > greenMax):
                    return False
            elif(color[1] == 'blue'):
                blue = int(color[0])
                if(blue > blueMax):
                    return False
    return True

sum = 0
for i, game in enumerate(games):
    if(gameIsPossible(game)):
        print("Game", i+1, "is possible")
        sum += i+1
    else:
        print("Game", i+1, "is not possible")

print("Sum of possible games:", sum)