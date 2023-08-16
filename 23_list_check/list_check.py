def list_check(lst):
    is_list = []
    for item in lst:
        is_list.append(isinstance(item, list))

    return all(is_list)    


    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
