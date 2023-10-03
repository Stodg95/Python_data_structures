def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    # create a new list
    # loop through the list
    # if the index is even, add the item to the new list
    # return the new list
    new_lst = []

    for i in range(len(lst)):
        if i % 2 == 0:
            new_lst.append(lst[i])

    return new_lst