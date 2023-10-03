def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """
    # create a variable to hold the sum
    # loop through the numbers in nums
    # if the number is a float, add it to the sum
    # return the sum
    sum = 0

    for num in nums:
        if type(num) == float:
            sum += num

    return sum
    