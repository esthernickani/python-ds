def flip_case(phrase, to_swap):
    flipped_case = ""
    for letter in phrase:
        if letter.lower() == to_swap or letter.upper() == to_swap:
            flipped_case += letter.swapcase()
        else:
            flipped_case += letter
    return flipped_case
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
