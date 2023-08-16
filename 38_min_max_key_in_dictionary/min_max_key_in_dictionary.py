def min_max_keys(d):
    key_lst = []
    for key in d.keys():
        key_lst.append(key)
    key_lst.sort()
    t = (key_lst[0], key_lst[-1])
    return t
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """