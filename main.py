import numpy as np
import matplotlib.pyplot as plt
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

    show_route(c, shortest_route)


def get_length(d, route):
    """Return the length of a route.

    Arguments:
    d -- matrix that contains distance between cities
    route -- array that contains the order of cities to visit
    """
    length = 0
    for i, j in zip(route, np.roll(route, -1)):
        length += d[i][j]
    return length


def show_route(c, route):
    """Show given route graphically.

    Arguments:
    c -- coordinates of the cities
    route -- route to be shown
    """
    plt.scatter(c[:, 0], c[:, 1])
    r = route + [route[0]]
    x = rearrange(c[:, 0], r)
    y = rearrange(c[:, 1], r)
    plt.plot(x, y)
    plt.show()


def rearrange(array, order):
    """Rearrange an array in given order.

    Arguments:
    array -- array that is rearranged
    order -- order in which the array to be rearranged

    Return:
    rearranged array
    """
    return [array[i] for i in order]


if __name__ == '__main__':
    main()
