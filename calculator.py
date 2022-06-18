import itertools
import crossbreed


def best_outcome(final):
    final_points = []
    for i in range(len(final)):
        points = 0
        w = 0
        x = 0
        h = 0
        y = 0
        g = 0
        for j in range(len(final[i])):
            if 'W' in str(final[i][j]):
                w += 1
                points -= 1
            elif 'X' in str(final[i][j]):
                x += 1
                points -= 1
            elif 'Y' in str(final[i][j]):
                if y == 0:
                    points += 0.9
                elif y == 1:
                    points += 0.8
                elif y == 2:
                    points += 0.7
                else:
                    points += 0.6
                y += 1
            elif 'H' in str(final[i][j]):
                h += 1
                points += 0.5
            elif 'G' in str(final[i][j]):
                if g == 0:
                    points += 0.9
                elif g == 1:
                    points += 0.8
                elif g == 2:
                    points += 0.7
                else:
                    points += 0.6
                g += 1
            if len(final[i][j]) > 2:
                points -= 3
        final_points.append(points)
    return final_points.index(max(final_points))


def calc_iterations(stuff, genetic_v):
    k = 0
    result_final = []
    all_results = []
    for L in range(2, 5):
        for subset in itertools.combinations(stuff, L):
            all_results.append(subset)
            k += 1
            test = []
            for gene in range(len(subset)):
                test.append(subset[gene].genetic)
            result = crossbreed.crossbreed(subset, genetic_v)
            # result_final = result_final + (result,)
            result_final.append(result)
    fp = best_outcome(result_final)
    final_post = []
    for s in range(len(all_results[fp])):
        final_post.append(all_results[fp][s].genetic)
    print("Best outcome: ", fp,  result_final[fp], "from this crossbreed: ", final_post)
    return result_final[fp], final_post


if __name__ == "__main__":
    lft = [1]
    genetic_value = {
        "W": 0,
        "X": 0,
        "Y": 0,
        "G": 0,
        "H": 0
    }
    calc_iterations(lft, genetic_value)
