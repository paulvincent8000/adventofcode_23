import pandas as pd

path = '/Users/paulvincent/Library/CloudStorage/OneDrive-InterWorks,Inc/Python/adventofcode_23/03/'
#input_file = 'part 1 sample.csv'
input_file = "part 1 input.csv"

with open(path + input_file) as f:                                  # Read in the data
    lines = [x.strip() for x in f.readlines()]

df = pd.DataFrame([list(line + '.') for line in lines],dtype=str)   # Build the schematic as a dataframe. Add extra column of dots to hand number in the final column


# test if character is next to an asterix
def touches_asterix(dataframe, row, col):
    rows = range(max(0, row-1),min(row+2,len(df)))
    cols = range(max(0, col-1),min(col+2,len(df.columns)))
    for rw in rows:
        for cl in cols:
            character = df.iloc[rw,cl]
            if character.isdigit():
                type_flag = 'digit'
            elif character == '*':
                type_flag = 'asterix'
                return rw,cl
            else:
                type_flag = 'dot'
    return


# step through dataframe and build numbers part II
partial_result = []
for row in range(len(df)):
    number = '0'
    valid = ()
    for col in range(len(df.columns)):
        character = df.iloc[row,col]
        if character.isdigit():
            number += character
            if type(touches_asterix(df,row,col)) == tuple:
                valid = touches_asterix(df,row,col) 
        else:
            if int(number) > 0 and len(valid) > 0:
                #print(int(number), valid)
                partial_result.append([valid, int(number)])
            number  = '0'
            valid = ()


# Build a list of asterix locations
asterix_locations = set([x[0] for x in partial_result])

z = 0
for asterix_location in asterix_locations:
    x = []
    for result in partial_result:
        if asterix_location == result[0]:
            x.append(result[1])
    #print(asterix_location, x)
    if len(x) == 2:
        z += x[0] * x[1]

print(f'Part II solution: {z}')