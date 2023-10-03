def repeat(phrase, num):
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
    # create a variable to hold the repeated phrase
    # loop through the range of num
    # add the phrase to the repeated phrase
    # return the repeated phrase
    repeated_phrase = ''

    if type(num) != int or num < 0:
        return None

    for i in range(num):
        repeated_phrase += phrase

    return repeated_phrase