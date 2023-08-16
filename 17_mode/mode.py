def mode(nums):
    nums_dict = {}
    
    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1


    count_lst = list(nums_dict.values())
    count_lst.sort()

    for (k,v) in nums_dict.items():
        if v == count_lst[-1]:
            return k

    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """