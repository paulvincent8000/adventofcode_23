path = '/Users/paulvincent/Library/CloudStorage/OneDrive-InterWorks,Inc/Python/adventofcode_23/02/'
#input_file = 'part 1 sample.csv'
input_file = "part 1 input.csv"
sum_calibration_values = 0

max_cubes = {'red':12, 'green':13, 'blue':14}
score = 0

with open(path + input_file) as f:                              # Read in the data
    lines = [x.strip() for x in f.readlines()]

for n, game in [x.split(': ') for x in lines]:                  # Start checking each game
    game_id = int(n.split(' ')[1])
    valid_game = True

    for pick in game.split('; '):                               # Start checking each handful of cubes

        for cube in pick.split(', '):                           # Check each cube
            n, colour = cube.split(' ')
            if int(n) > max_cubes[colour]:                      # Test for invalid number of cubes
                valid_game = False

    
    if valid_game:                                              # If the game is valid
        score += game_id                                        # Add the game number to the score    

print(f'The score for part I is {score}')
