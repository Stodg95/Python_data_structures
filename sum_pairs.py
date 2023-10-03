def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    # create a set to hold the numbers we've seen
    # loop through the numbers in nums
    # subtract the current number from the goal
    # if the result is in the set, return the tuple of the current number and the result
    # otherwise, add the current number to the set
    # if we get through the loop without returning, return an empty tuple
    seen = set()

    for num in nums:
        result = goal - num

        if result in seen:
            return (result, num)
        else:
            seen.add(num)

    return ()