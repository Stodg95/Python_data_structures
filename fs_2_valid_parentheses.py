def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    
        # create a counter
        # iterate over the string
        # if the character is a (, add 1 to the counter
        # if the character is a ), subtract 1 from the counter
        # if the counter is ever negative, return False
        # if the counter is 0 at the end, return True
        # otherwise, return False
    
    counter = 0
    
    for char in parens:
            if char == "(":
                counter += 1
            elif char == ")":
                counter -= 1
            if counter < 0:
                return False
    
    return counter == 0