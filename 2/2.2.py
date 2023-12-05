import input

"""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

string = input.input



games = string.split('\n')

def gameMinCubesPower(game):
    game = game.split(':')[1]
    game = game.split(';')
    redMin = 0
    greenMin = 0
    blueMin = 0
    for round in game:
        round = round.split(',')
        for color in round:
            color = color.strip()
            color = color.split(' ')
            if(color[1] == 'red'):
                red = int(color[0])
                if(red > redMin):
                    redMin = red
            elif(color[1] == 'green'):
                green = int(color[0])
                if(green > greenMin):
                    greenMin = green
            elif(color[1] == 'blue'):
                blue = int(color[0])
                if(blue > blueMin):
                    blueMin = blue
    print(redMin * greenMin * blueMin)
    return redMin * greenMin * blueMin

sum = 0
for i, game in enumerate(games):
    sum += gameMinCubesPower(game)

print("Sum of possible games:", sum)