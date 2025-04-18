def Identity_Operators():
    """This function demonstrates the examples of identity operators in Python."""

    # Heading
    print("\nIdentity Operators: -\n")

    a: list = [1, 2, 3]
    b: list = [1, 2, 3]
    c = a

    # Is
    print("Is:")
    result = a is c
    print("The id of a is", id(a))
    print("The id of c is", id(c))
    print(f"Example: {a} is {c} = {result}\n")

    # Is not
    print("Is not:")
    result = a is not b
    print("The id of a is", id(a))
    print("The id of c is", id(b))
    print(f"Example: {a} is not {b} = {result}\n")