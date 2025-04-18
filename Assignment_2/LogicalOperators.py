def Logical_Operators(x, y):
    """This function demonstrates the examples of logical operators in Python."""

    # Heading
    print("\nLogical Operators: -\n")

    # Logical AND
    print("Logical AND:")
    result = (x <= y) and (x > y)
    print(f"Example: ({x} <= {y}) and ({x} > {y}) = {result}\n")

    # Logical OR
    print("Logical OR:")
    result = (x != y) or (x >= y)
    print(f"Example: ({x} != {y}) or ({x} >= {y}) = {result}\n")

    # Logical NOT
    print("Logical NOT:")
    result = not (x > y)
    print(f"Example: not ({x} > {y}) = {result}\n")