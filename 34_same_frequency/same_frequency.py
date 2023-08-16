def same_frequency(num1, num2):
    lst_1 = list(str(num1))
    lst_2 = list(str(num2))
    
    lst_1.sort()
    lst_2.sort()

    if lst_1 == lst_2:
        return True 
    else:
        return False
    
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """