def repeat(phrase, num):
    lst = []
    if num == 0:
        return ""
    elif type(num) != int or num < 0:
        return None

    for x in range(num):
        lst.append(phrase)
        print(lst)
    repeated_phrase = ''.join(lst)
    return repeated_phrase
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
