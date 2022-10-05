def sum(first, second):
    """
    Returns the sum of two decimal numbers
    Parameters:
                    first : A decimal number
                    second : Another decimal number
    Returns:
                    sum_of_input (str): string of the sum of first and second
    """
    sum_of_input = str(first + second)
    return sum_of_input


print(sum(10, 20.50))
print(sum.__doc__)
