path = '/Users/paulvincent/Library/CloudStorage/OneDrive-InterWorks,Inc/Python/adventofcode_23/01/'
#input_file = "part 1 sample.csv"
input_file = "part 1 input.csv"
sum_calibration_values = 0

def reader(input_file):
    with open(input_file) as f:
        return f.readlines()

def get_digits(text):
    return list( filter(str.isdigit, text) )

def get_first_digit(text):
    return text[0]

def get_last_digit(text):
    return(text[-1])

lines = reader(path + input_file)

for line in lines:
    digits = get_digits(line)
    calibration_value = int( get_first_digit(digits) + get_last_digit(digits) )
    sum_calibration_values += calibration_value
    print( calibration_value )
print(f'The value is {sum_calibration_values}')