path = '/Users/paulvincent/Library/CloudStorage/OneDrive-InterWorks,Inc/Python/adventofcode_23/02/'
#input_file = 'part 1 sample.csv'
input_file = "part 1 input.csv"


result = 0

with open(path + input_file) as f:                              # Read in the data
    lines = [x.strip() for x in f.readlines()]

for n, game in [x.split(': ') for x in lines]:                  # Start checking each game
    game_id = int(n.split(' ')[1])

    max_cubes = {'red':1, 'green':1, 'blue':1}

    for pick in game.split('; '):                               # Start checking each handful of cubes

        for cube in pick.split(', '):                           # Check each cube
            n, colour = cube.split(' ')

            if int(n) > max_cubes[colour]:                      # If the number of cubes is higher than before
                max_cubes[colour] = int(n)                      # Update the maximum for the respective colour

    # print(game, max_cubes, result)

    result += max_cubes["red"] * max_cubes['green'] * max_cubes['blue']

print(result)
