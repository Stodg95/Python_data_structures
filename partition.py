def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    # create a list to hold the partitioned list
    # create a list to hold the items that pass the test
    # create a list to hold the items that fail the test
    # loop through the list
    # if the item passes the test, add it to the pass list
    # otherwise, add it to the fail list
    # add the pass and fail lists to the partitioned list
    # return the partitioned list

    pass_lst = []
    fail_lst = []

    for item in lst:
        if fn(item):
            pass_lst.append(item)
        else:
            fail_lst.append(item)

    return [pass_lst, fail_lst]