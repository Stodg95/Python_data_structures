def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # split the phrase into a list of words
    # loop through the words
    # capitalize each word
    # join the words back together
    # return the phrase
    words = phrase.split(' ')

    for i in range(len(words)):
        words[i] = words[i].capitalize()

    return ' '.join(words)