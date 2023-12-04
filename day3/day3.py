import re

def read_input(filename):
    with open(filename) as file:
        lines = ['.' + line.rstrip() + '.' for line in file]
        # for line in lines:
            # if lines.index(line) == 0:
        lines.insert(0, '.' * len(lines[1]))
            # if lines.index(line) == len(lines)-1:
        lines.insert(len(lines), '.' * len(lines[1]))
                # break
        return lines

def process(lines):
    sum = 0
    num_span_cords_list = []
    sym_span_cords_list = []
    for row_idx, row in enumerate(lines):
        num_span_cords_list.append([row_idx, [(m.start(0), m.end(0)) for m in re.finditer('\d+', row)]])
        sym_span_cords_list.append([row_idx, [(m.start(0), m.end(0)) for m in re.finditer('[^a-zA-Z0-9.]', row)]])
    for num_span_cords in num_span_cords_list:
        row = num_span_cords[0]
        span_list = num_span_cords[1]
        for span in span_list:
            adj_string = lines[row-1][span[0]-1:span[1]+1] + lines[row][span[0]-1:span[1]+1] + lines[row+1][span[0]-1:span[1]+1]
            if re.search('[^a-zA-Z0-9.]', adj_string):
                sum += int(lines[row][span[0]:span[1]])
    print('TOTAL SUM IS ' + str(sum))

def main():
    input_dir = r'aoc-2023\day3\inputs\input.txt'
    input = read_input(input_dir)
    process(input)

if __name__ == "__main__":
    main()