import numpy as np
import random as random



def ER(n,p):
    """
    :param n: number of nodes
    :param p: probability to generate an edge
    :return: Graph
    """
    G = np.zeros((n, n))
    count = 0
    for row in range(n):
        for col in range(n):
            a = random.uniform(0, 1)
            if a < p and G[row][col] != 1 and row != col:
                G[row][col] = 1
                count += 1
    return G, count

def findP(G):
    for p in np.arange(0.000314, 0.0003198, 0.000001):
        G, count = ER(6474, p)
        print("{} \t {}".format(p, count))


def main():
    for p in np.arange(0.000314, 0.0003198, 0.000001):
        G, count = ER(6474, p)
        print("{} \t {}".format(p, count))

if __name__=='__main__':
    main()









