def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        return lines

def process(input, valid_digits):
    sum = 0 
    for line in input:
        for kv in valid_digits.items():
            if kv[1] in line:
                line = line.replace(kv[1], kv[0]) 
        nums = [int(c) for c in line if c.isdigit()]
        sum += int(str(nums[0]) + str(nums[-1]))
    return sum

def main():
    valid_digits = {'18':'oneight', '21':'twone', '38':'threeight', '58':'fiveight',
                    '79':'sevenine', '82':'eightwo', '98':'nineight', '1': 'one',
                    '2':'two', '3':'three', '4': 'four', '5':'five', '6': 'six', 
                    '7': 'seven', '8':'eight', '9': 'nine'}
    input_dir = r'inputs\input.txt'
    input = read_input(input_dir)
    sum = process(input, valid_digits)
    print(sum)

if __name__ == "__main__":
    main()