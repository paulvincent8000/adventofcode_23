path = '/Users/paulvincent/Library/CloudStorage/OneDrive-InterWorks,Inc/Python/adventofcode_23/01/'
#input_file = "part 1 sample.csv"
#input_file = "part 2 sample.csv"
input_file = "part 1 input.csv"
#input_file = "part 1 input.csv"

def reader(input_file):
    with open(input_file) as f:
        return f.readlines()

def find_numbers(text):
    hidden_digits = []
    for x, y in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        search_text = y
        search_value = x+1
        position = text.find(search_text)
        if position >= 0:
            hidden_digits.append([position,search_value])
    return hidden_digits

def replace_numbers(text, replacement_string):
    # convert text to a list
    input_list = list(text)
    # replace first character with number
    if len(replacement_string) == 0:
        return text
    for x in replacement_string:
        input_list[ x[0] ] = str( x[1] )
    # convert back to text
    return ''.join(input_list)

def get_calibration_value(text):
    # extract digits only
    digits = list( filter(str.isdigit, text) )
    # extract first and last digits
    return int( digits[0] + digits[-1] )


lines = reader(path + input_file)

# Clean line ends from the input
clean_lines = [line.strip('\n') for line in lines]

calibration_code = 0
for line in clean_lines:
    numbers0 = find_numbers(line)
    updated_line0 = replace_numbers(line,numbers0)
    numbers1 = find_numbers(updated_line0)
    updated_line1 = replace_numbers(updated_line0,numbers1)
    numbers = find_numbers(updated_line1)
    updated_line = replace_numbers(updated_line1,numbers)
    calibration_code += get_calibration_value(updated_line)
    #print(line, get_calibration_value(updated_line))
print(f'The calibration code is {calibration_code}')
