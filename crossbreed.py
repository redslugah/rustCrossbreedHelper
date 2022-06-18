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
        for j in range(len(seeds)):
            gene = gene + ((seeds[j].genetic[i]),)
        value = crossbreed_calc(gene, value)
        max_keys = (key for key, values in value.items() if values == max(value.values()))
        max_keys = list(max_keys)
        final = final + (max_keys,)
    # print(final)
    return final
