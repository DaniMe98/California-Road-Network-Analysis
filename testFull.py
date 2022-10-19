import numpy as np
from tqdm import tqdm


def sort(d,a):

    print("Creazione dizionario ")

    with open('C:/Users/danil/Downloads/magistrale/Social Network Analysis/Project/FullRoadNoDupCount.txt') as f:
        for line in f:
            (key, val) = line.split()
            d[int(key)] = val
            
    print("Dizionario creato \n")

    a = sorted(d.items(), key=lambda x: x[1], reverse=True)


    with open('SortedFullRoadNoDupCount.txt', 'w') as f:
            for y in tqdm(a):
                line = str(y)#[str(y),str(a[y])]
            #    tab = '\t' 
            #    lines = tab.join(line)
                f.write(line + '\n')
    print("Salvataggio dizionario completo")