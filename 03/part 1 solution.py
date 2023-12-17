import pandas as pd

path = '/Users/paulvincent/Library/CloudStorage/OneDrive-InterWorks,Inc/Python/adventofcode_23/03/'
#input_file = 'part 1 sample.csv'
input_file = "part 1 input.csv"

with open(path + input_file) as f:                                  # Read in the data
    lines = [x.strip() for x in f.readlines()]

df = pd.DataFrame([list(line + '.') for line in lines],dtype=str)   # Build the schematic as a dataframe. Add extra column of dots to hand number in the final column

# create function to test if character is next to a symbol
def touches_symbol(dataframe, row, col):
    rows = range(max(0, row-1),min(row+2,len(df)))
    cols = range(max(0, col-1),min(col+2,len(df.columns)))
    for rw in rows:
        for cl in cols:
            character = df.iloc[rw,cl]
            if character.isdigit():
                type_flag = 'digit'
            elif character != '.':
                type_flag = 'symbol'
                return 1
            else:
                type_flag = 'dot'
    return 0

# step through dataframe and build numbers
result = 0
for row in range(len(df)):
    number = '0'
    valid = [0]
    for col in range(len(df.columns)):
        character = df.iloc[row,col]
        if character.isdigit():
            number += character
            valid.append(touches_symbol(df,row,col) )
        else:
            #print(int(number), max(valid))
            result += int(number) * max(valid)
            number  = '0'
            valid = [0]



print(f'Part I solution: {result}')