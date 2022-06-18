import calculator
import main


def time_to_perfect_it(seeds, genetic_value):
    crossbreed_sequence = []
    da_list = ()
    result_seed, crossbreed_seeds = calculator.calc_iterations(seeds, genetic_value)
    crossbreed_sequence.append(crossbreed_seeds)
    for i in range(len(result_seed)):
        da_list = da_list + (result_seed[i][0],)
    # print("Resultado: ", result_seed, "Realizado crossbreed com as seguintes sementes: ", crossbreed_seeds)
    # print("Resultado filtrado: ", da_list, "Realizado crossbreed com as seguintes sementes: ", crossbreed_seeds)
    g_value = 0
    y_value = 0
    for j in da_list:
        if j == 'G':
            g_value += 1
        if j == 'Y':
            y_value += 1
    if y_value < 4 or g_value < 2:
        print("Realizando próximo crossbreed... ")
        seeds.append(main.Seed(seeds[-1].order + 1, da_list))
        time_to_perfect_it(seeds, genetic_value)
    else:
        print("Resultado 2g4y. Encerrando programa...")
