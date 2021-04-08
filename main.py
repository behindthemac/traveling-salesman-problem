import numpy as np
from scipy.spatial import distance
from permutations import circular_permutations


def main():
    n = 10
    c = np.random.randn(n, 2)
    d = [[distance.euclidean(c[i], c[j]) for j in range(n)] for i in range(n)]

    routes = circular_permutations(list(range(n)))


if __name__ == '__main__':
    main()
