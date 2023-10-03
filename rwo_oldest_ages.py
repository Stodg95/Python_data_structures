def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """
    # create a set to hold the oldest ages
    # loop through the ages
    # if the age is greater than the first oldest age, add it to the set
    # if the age is greater than the second oldest age, add it to the set
    # return the tuple of the second oldest age and the oldest age
    oldest_ages = set()
    oldest_age = 0
    second_oldest_age = 0

    for age in ages:
        if age > oldest_age:
            second_oldest_age = oldest_age
            oldest_age = age
            oldest_ages.add(oldest_age)
        elif age > second_oldest_age:
            second_oldest_age = age
            oldest_ages.add(second_oldest_age)

    return (second_oldest_age, oldest_age)

