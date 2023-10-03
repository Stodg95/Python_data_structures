def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    # create a set to hold the numbers we've seen
    # loop through the numbers in nums
    # if we find a number that's already in the set, return it
    # otherwise, add it to the set
    # if we get through the loop, then there was no duplicate
    # so return None
    seen = set()

    for num in nums:
        if num in seen:
            return num
        else:
            seen.add(num)

    return None