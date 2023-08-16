def sum_up_diagonals(matrix):
    num_to_add = []
    for lst in matrix:
        current_idx = matrix.index(lst)
        num_to_add.append(lst[current_idx])
        lst.reverse()
        num_to_add.append(lst[current_idx])
    
    sum = 0
    for num in num_to_add:
        sum += num
    return sum
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """