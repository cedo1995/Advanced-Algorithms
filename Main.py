import numpy as np
import random as random
from decimal import Decimal

def ER(n,p):
    """
    :param n: number of nodes
    :param p: probability to generate an edge
    :return: Graph
    """
    random.seed(2)
    G = np.zeros((n, n))
    count = 0
    for row in range(n):
        for col in range(n):
            a = random.uniform(0, 1)
            if a < p and G[col][row] != 1 and row != col: #con G[col][row] != 1 non considero i doppi archi avendo un grafo non orientato
                G[row][col] = 1
                count += 1
    return G, count
"""
def findP(G):
    for p in np.arange(0.000314, 0.0003198, 0.000001):
        G, count = ER(6474, p)
        print("{} \t {}".format(p, count))
"""

def bisectionMethod(a,b,tolerance):
    G1, count1 = ER(6474, a)

    if (abs(count1 - 13233) > tolerance):
        G2, count2 = ER(6474, b)

        if (abs(count2 - 13233) > tolerance):
                    m = (a+b) / 2
                    if abs(count1-13233) < abs(count2-13233):
                        print(" intervallo",a," ",m)
                        return bisectionMethod(a, m, scarto)
                    else:
                        print(" intervallo",m," ",b)
                        return bisectionMethod(m, b, scarto)
        else:
            return Decimal(b)
    else:
        return Decimal(a)






def main():
    """a=float(0.0)
    b=float(1.0)
    tolerance = 20      ##da valutare se cambiarlo
    p= Decimal(bisectionMethod(a,b,tolerance))
    print("probability: ",p)
    """
    #calcolo di p ideale
    numNodes = 6474
    numEdges = 13233
    p = numEdges / (numNodes**2)
    G, count = ER(numNodes, p)
    print(count,p)
    #read data from file
    """data = np.loadn('./as20000102.txt', encoding = int)
    startingNode = data[:,0]
    endingNode = data[:,1]

    print( "{}\t{}".format(startingNode, endingNode) )

    """

    """for p in np.arange(0.000314, 0.0003198, 0.000001):
        G, count = ER(6474, p)
        print("{} \t {}".format(p, count))
    """


if __name__=='__main__':
    main()
