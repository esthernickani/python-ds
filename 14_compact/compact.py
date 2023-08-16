def compact(lst):
    true_lst = []
    for element in lst:
        if bool(element) == True:
            true_lst.append(element)
    return true_lst
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """