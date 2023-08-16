def sum_range(nums, start=0, end=None):
    sum = 0
    if start == 0 and end == None:
        for num in nums:
            sum += num
        return sum
    elif start != 0 and end == None:
        lst = nums[start::]
        for num in lst:
            sum += num
        return sum
    elif start == 0 and end != None:
        lst = nums[:end+1:]
        for num in lst:
            sum += num
        return sum
    elif start != 0 and end > len(nums):
        lst = nums[start::]
        for num in lst:
            sum += num
        return sum
    elif start != 0 and end != 0:
        lst = nums[start:end+1:]
        for num in lst:
            sum += num
        return sum
    
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
