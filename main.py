import extractor
import imageGrabber
import keyboard


class Seed:
    def __init__(self, order, genetic):
        self.genetic = genetic
        self.order = order


def crossbreed_calc(gene, value):
    if gene is None:
        return
    for i in gene:
        if i == "W":
            value[i] += 1
        if i == "X":
            value[i] += 1
        if i == "Y":
            value[i] += 0.6
        if i == "H":
            value[i] += 0.6
        if i == "G":
            value[i] += 0.6
    return value


def crossbreed(seeds, value):
    final = ()
    for i in range(6):
        gene = ()
        for key, values in value.items():
            value[key] = 0
        for j in seeds:
            gene = gene + ((seeds[j].genetic[i]),)
        crossbreed_calc(gene, value)
        max_keys = (key for key, values in value.items() if values == max(value.values()))
        max_keys = list(max_keys)
        final = final + (max_keys,)
    print(final)


def main():
    genetic_value = {
        "W": 0,
        "X": 0,
        "Y": 0,
        "G": 0,
        "H": 0
    }
    numb = int(input("quantas seeds?"))
    seeds = {}
    place = input("1-ground, 2-inventory")
    for i in range(numb):
        br = 1
        while br == 1:
            if keyboard.is_pressed('ctrl'):
                genetic = ()
                imageGrabber.grab_image(place)
                genetic = genetic + extractor.image_read()
                seeds[i] = Seed(i, genetic)
                print(seeds[i].order + 1, seeds[i].genetic)
                br = 0
    crossbreed(seeds, genetic_value)


if __name__ == "__main__":
    main()
