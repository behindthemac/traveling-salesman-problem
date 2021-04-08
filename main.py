import numpy as np
from scipy.spatial import distance
from permutations import circular_permutations


def main():
    n = 10
    c = np.random.randn(n, 2)
    d = [[distance.euclidean(c[i], c[j]) for j in range(n)] for i in range(n)]

    routes = circular_permutations(list(range(n)))
    shortest_route = next(routes)
    shortest_length = get_length(d, shortest_route)
    for route in routes:
        length = get_length(d, route)
        if length < shortest_length:
            shortest_route = route
            shortest_length = length


def get_length(d, route):
    """Return the length of given route.

    Arguments:
    d -- matrix that contains distance between cities
    route -- array that contains the order of cities to visit

    Return:
    length -- length of given route
    """
    length = 0
    for i, j in zip(route, np.roll(route, -1)):
        length += d[i][j]
    return length


if __name__ == '__main__':
    main()
