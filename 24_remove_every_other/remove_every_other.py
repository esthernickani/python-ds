def remove_every_other(lst):
    other_list = []
    length = len(lst)
    for num in range(0,length,2):
        other_list.append(lst[num])
    return other_list
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
