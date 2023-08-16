def truncate(phrase, n):
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    else: 
        if len(phrase) >= n:
            s = list(phrase)
            trunc_lst = s[0:n]
            print(n)
            trunc_lst[-1] = "."
            trunc_lst[-2] = "."
            trunc_lst[-3] = "."
            trunc_phrase = ''.join(trunc_lst)
            return trunc_phrase
        else:
            return phrase

    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """