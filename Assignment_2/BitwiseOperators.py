def Bitwise_Operators(x, y):
    """This function demonstrates the examples of bitwise operators in Python."""

    # Heading
    print("\nBitwise Operators: -\n")

    # Bitwise AND
    print("Bitwise AND:")
    result = x & y
    print(f"Example: {x} & {y} = {result}\n")

    # Bitwise OR
    print("Bitwise OR:")
    result = x | y
    print(f"Example: {x} | {y} = {result}\n")

    # Bitwise XOR
    print("Bitwise XOR:")
    result = x ^ y
    print(f"Example: {x} ^ {y} = {result}\n")

    # Bitwise NOT
    print("Bitwise NOT:")
    result = ~(x > y)
    print(f"Example: ~({x} > {y}) = {result}\n")

    # Bitwise Left Shift
    print("Bitwise Left Shift:")
    result = x << y
    print(f"Example: {x} << {y} = {result}\n")

    # Bitwise Right Shift
    print("Bitwise Right Shift:")
    result = x >> y
    print(f"Example: {x} >> {y} = {result}\n")