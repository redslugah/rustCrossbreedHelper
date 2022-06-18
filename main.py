import extractor
import imageGrabber
import calculator
import crossbreed
import keyboard


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
    numb = int(input("quantas seeds?"))
    module = int(input("1- calcular possibilidades, 2- testar crossbreed"))
    # seeds = {}
    seeds = []
    place = int(input("1-ground, 2-inventory"))
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
    else:
        print(crossbreed.crossbreed(seeds, genetic_value))


if __name__ == "__main__":
    main()
