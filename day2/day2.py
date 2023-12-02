def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        return lines

def process(input, cube_cnt):
    game_sum = 0
    power_sum = 0
    for game in input:
        curr_game = int(game[game.index('e')+1 : game.index(':')])
        max_cube_cnt = {'red':0, 'green':0, 'blue':0}
        isValid = True
        for rnd in game.split(';'):
            rnd_cnt = {'red':0, 'green':0, 'blue':0}
            for k in rnd_cnt.keys():
                if k in rnd:
                    rnd_cnt[k] = rnd_cnt[k] + int(rnd[rnd.index(k)-3 : rnd.index(k)-1])
                    if rnd_cnt[k] > max_cube_cnt[k]:
                        max_cube_cnt[k] = rnd_cnt[k]
                    if rnd_cnt[k] > cube_cnt[k]:
                        isValid = False
        if isValid:
            game_sum += curr_game
        power_sum += max_cube_cnt['red'] * max_cube_cnt['green'] * max_cube_cnt['blue']
    print("Power sum is " + str(power_sum))
    print("Game sum is " + str(game_sum))

def main():
    cube_cnt = {'red':12, 'green':13, 'blue':14}
    input_dir = r'inputs\input.txt'
    input = read_input(input_dir)
    process(input, cube_cnt)

if __name__ == "__main__":
    main()