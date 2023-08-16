def number_compare(a, b):
    if b == a:
        return 'Numbers are equal'
    elif a > b:
        return 'First is greater'
    elif b > a:
        return 'Second is greater'
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """