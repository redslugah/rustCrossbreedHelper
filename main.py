import extractor
import imageGrabber
import calculator
import crossbreed
import keyboard
import perfecter


class Seed:
    def __init__(self, order, genetic):
        self.genetic = genetic
        self.order = order


def main():
    genetic_value = {
        "W": 0,
        "X": 0,
        "Y": 0,
        "G": 0,
        "H": 0
    }
    numb = int(input("seeds"))
    module = int(input("1- calcular possibilidades, 2- testar crossbreed, 3- perfect breeder"))
    # seeds = {}
    seeds = []
    place = int(input("1-ground, 2-inventory"))
    '''
    # seeds info for testing. 56 seeds
    seeds.append(Seed(1, ('X', 'G', 'Y', 'Y', 'Y', 'H')))
    seeds.append(Seed(2, ('X', 'G', 'G', 'Y', 'G', 'H')))
    seeds.append(Seed(3, ('X', 'G', 'H', 'W', 'Y', 'H')))
    seeds.append(Seed(4, ('X', 'H', 'Y', 'X', 'H', 'X')))
    seeds.append(Seed(5, ('W', 'H', 'G', 'H', 'H', 'H')))
    seeds.append(Seed(6, ('W', 'H', 'G', 'X', 'X', 'W')))
    seeds.append(Seed(7, ('X', 'Y', 'G', 'X', 'W', 'W')))
    seeds.append(Seed(8, ('H', 'H', 'Y', 'X', 'H', 'H')))
    seeds.append(Seed(9, ('X', 'G', 'Y', 'Y', 'Y', 'H')))
    seeds.append(Seed(10, ('X', 'Y', 'H', 'G', 'W', 'W')))
    seeds.append(Seed(11, ('W', 'Y', 'H', 'X', 'Y', 'X')))
    seeds.append(Seed(12, ('W', 'Y', 'H', 'W', 'G', 'Y')))
    seeds.append(Seed(13, ('X', 'Y', 'G', 'X', 'Y', 'H')))
    seeds.append(Seed(14, ('W', 'G', 'Y', 'W', 'H', 'H')))
    seeds.append(Seed(15, ('W', 'H', 'W', 'X', 'H', 'H')))
    seeds.append(Seed(16, ('W', 'Y', 'H', 'X', 'G', 'X')))
    seeds.append(Seed(17, ('W', 'H', 'G', 'X', 'Y', 'W')))
    seeds.append(Seed(18, ('Y', 'H', 'G', 'X', 'W', 'H')))
    seeds.append(Seed(19, ('G', 'X', 'Y', 'W', 'W', 'X')))
    seeds.append(Seed(20, ('W', 'W', 'Y', 'X', 'H', 'X')))
    seeds.append(Seed(21, ('W', 'G', 'H', 'W', 'Y', 'H')))
    seeds.append(Seed(22, ('W', 'H', 'X', 'X', 'H', 'W')))
    seeds.append(Seed(23, ('W', 'H', 'Y', 'W', 'H', 'W')))
    seeds.append(Seed(24, ('H', 'W', 'G', 'W', 'H', 'H')))
    seeds.append(Seed(25, ('X', 'H', 'G', 'W', 'H', 'H')))
    seeds.append(Seed(26, ('H', 'H', 'W', 'X', 'X', 'W')))
    seeds.append(Seed(27, ('Y', 'H', 'X', 'X', 'G', 'H')))
    seeds.append(Seed(28, ('W', 'X', 'Y', 'Y', 'G', 'X')))
    seeds.append(Seed(29, ('W', 'W', 'Y', 'X', 'H', 'H')))
    seeds.append(Seed(30, ('X', 'Y', 'Y', 'X', 'X', 'W')))
    seeds.append(Seed(31, ('X', 'H', 'Y', 'X', 'H', 'H')))
    seeds.append(Seed(32, ('H', 'G', 'Y', 'W', 'Y', 'X')))
    seeds.append(Seed(33, ('W', 'X', 'Y', 'Y', 'Y', 'H')))
    seeds.append(Seed(34, ('X', 'X', 'H', 'X', 'Y', 'W')))
    seeds.append(Seed(35, ('X', 'G', 'G', 'X', 'G', 'H')))
    seeds.append(Seed(36, ('W', 'G', 'W', 'W', 'Y', 'G')))
    seeds.append(Seed(37, ('X', 'Y', 'W', 'X', 'G', 'W')))
    seeds.append(Seed(38, ('X', 'Y', 'Y', 'H', 'G', 'X')))
    seeds.append(Seed(39, ('X', 'G', 'H', 'W', 'G', 'X')))
    seeds.append(Seed(40, ('W', 'G', 'X', 'X', 'Y', 'H')))
    seeds.append(Seed(41, ('X', 'Y', 'Y', 'G', 'H', 'Y')))
    seeds.append(Seed(42, ('Y', 'H', 'X', 'X', 'G', 'H')))
    seeds.append(Seed(43, ('X', 'Y', 'G', 'X', 'G', 'G')))
    seeds.append(Seed(44, ('X', 'G', 'H', 'G', 'W', 'X')))
    seeds.append(Seed(45, ('H', 'H', 'G', 'X', 'H', 'H')))
    seeds.append(Seed(46, ('W', 'X', 'Y', 'Y', 'G', 'X')))
    seeds.append(Seed(47, ('Y', 'G', 'H', 'X', 'G', 'W')))
    seeds.append(Seed(48, ('Y', 'H', 'G', 'W', 'G', 'W')))
    seeds.append(Seed(49, ('W', 'W', 'Y', 'X', 'G', 'X')))
    seeds.append(Seed(50, ('X', 'G', 'G', 'W', 'X', 'H')))
    seeds.append(Seed(51, ('H', 'G', 'Y', 'X', 'Y', 'W')))
    seeds.append(Seed(52, ('X', 'G', 'G', 'X', 'W', 'H')))
    seeds.append(Seed(53, ('X', 'G', 'G', 'W', 'H', 'H')))
    seeds.append(Seed(54, ('W', 'G', 'Y', 'X', 'G', 'X')))
    seeds.append(Seed(55, ('G', 'X', 'H', 'X', 'W', 'H')))
    seeds.append(Seed(56, ('W', 'G', 'G', 'H', 'H', 'W')))
    ''' 
    for i in range(numb):
        br = 1
        while br == 1:
            if keyboard.is_pressed('r'):
                genetic = ()
                imageGrabber.grab_image(place)
                genetic = genetic + extractor.image_read()
                # seeds[i] = Seed(i, genetic)
                seeds.append(Seed(i, genetic))
                print(seeds[i].order + 1, seeds[i].genetic)
                br = 0
    if module == 1:
        calculator.calc_iterations(seeds, genetic_value)
    elif module == 2:
        print(crossbreed.crossbreed(seeds, genetic_value))
    elif module == 3:
        perfecter.time_to_perfect_it(seeds, genetic_value)


if __name__ == "__main__":
    main()
