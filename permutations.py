def permutations(array, permutation=[]):
    """Generate all possible permutations of an array.

    Argument:
    array -- array that is permutated
    """
    n = len(array)
    if n > 0:
        for i in range(n):
            array_copy = array.copy()
            element = array_copy.pop(i)
            yield from permutations(array_copy, permutation + [element])
    else:
        yield permutation


def circular_permutations(array):
    """Generate all possible circular permutations of an array.

    Argument:
    array -- array that is permutated
    """
    permutation = [array.pop(0)]
    return permutations(array, permutation)
