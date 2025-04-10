import time

# ANSI escape codes for styling
bold_start = "\033[1m"
italic_start = "\033[3m"
end = "\033[0m"

# Data Types
def Data_Types():
    print(f"\n{bold_start}Data Types:{end}\n")

    # Int
    def Int():
        print(f"\n{bold_start}Int Type: -{end}")
        print("Definition: An integer is a whole number (not a fraction) that can be positive, negative, or zero. Integers are a common data type in computer programming. They are used to store whole numbers. For example, the number 10 is an integer.")
        x: int = 5
        result = x + 5
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # String
    def String():
        print(f"\n{bold_start}String Type: -{end}")
        print("Definition: A string is a sequence of characters enclosed in quotation marks. In Python, a string can be a sequence of any character, including letters, numbers, special characters, and whitespace. Strings are used to store text data in a program. For example, the string 'Hello, World!' is a string.\n")
        time.sleep(1)

        # Single Quote String
        print(f"{italic_start}Single Quotes String:{end}")
        single_quotes: str = 'Hello to Python\nFrom, Abdul Rehman Jiwani'
        print(f"Exmaple Result: {bold_start}'{single_quotes}'{end}\n")
        time.sleep(1)

        # Double Quote String
        print(f"{italic_start}Double Quotes String:{end}")
        double_quotes: str = "Hello to Python\nFrom, Abdul Rehman Jiwani"
        print(f'Example Result: {bold_start}"{double_quotes}"{end}\n')
        time.sleep(1)

        # Triple Quote String
        print(f"{italic_start}Triple Quotes String:{end}")
        triple_quotes: str = """Hello to Python
                                From, Abdul Rehman Jiwani"""
        print(f"Example Result: {bold_start}'''{triple_quotes}'''{end}\n")
        time.sleep(1)

    # Float
    def Float():
        print(f"\n{bold_start}Float Type: -{end}")
        print("Definition: A float is a floating-point number, which means it is a number that has a decimal point. Floats are used to store real numbers, such as 3.14, 0.001, or -2.5.")
        x: float = 2.5
        result = x + 5.5
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # Boolean
    def Boolean():
        print(f"\n{bold_start}Boolean Type: -{end}")
        print("Definition: A boolean is a data type that can have one of two values: True or False. Booleans are used to represent the truth values of logical expressions. For example, the expression 1 < 2 is True, while the expression 1 > 2 is False.")
        result = 1 < 2
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # List
    def List():
        print(f"\n{bold_start}List Type: -{end}")
        print("Definition: A list is a collection of items that are ordered and changeable. Lists are one of the most commonly used data types in Python. They are used to store multiple items in a single variable. For example, a list of numbers [1, 2, 3] or a list of strings ['apple', 'banana', 'cherry'].")
        result: list = [1, 2, 3, 4, 5]
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # Dictionary
    def Dict():
        print(f"\n{bold_start}Dictionary Type: -{end}")
        print("Definition: A dictionary is a collection of items that are unordered, changeable, and indexed. Dictionaries are used to store key-value pairs. For example, a dictionary of student information {'name': 'John', 'age': 20, 'city': 'New York'}.")
        student_info: dict = {"name": "Moiz", "age": 20, "city": "Karachi", "gender": "Male", "enrolled": False }
        print(f"Example Result: {bold_start}{student_info['name']}{end}\n")
        time.sleep(1)

    # Complex
    def Complex():
        print(f"\n{bold_start}Complex Type: -{end}")
        print("Definition: A complex number is a number that can be expressed in the form a + bi, where a and b are real numbers, and i is the imaginary unit. Complex numbers are used in mathematics and engineering to represent quantities that have both a real and an imaginary part. For example, the complex number 2 + 3i.")
        x: complex = 2j
        result = x + 5j
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # Tuple
    def Tuple():
        print(f"\n{bold_start}Tuple Type: -{end}")
        print("Definition: A tuple is a collection of items that are ordered and unchangeable. Tuples are similar to lists, but they are immutable, which means that once a tuple is created, its elements cannot be changed. For example, a tuple of numbers (1, 2, 3) or a tuple of strings ('apple', 'banana', 'cherry').")
        Tuple: tuple = (1, 2, 5, False, .69, "Hello", "Hello", True)
        print(f"Example Result: {bold_start}{Tuple}{end}\n")
        time.sleep(1)

    # Set
    def Set():
        print(f"\n{bold_start}Set Type: -{end}")
        print("Definition: A set is a collection of items that are unordered and unindexed. Sets are used to store multiple items in a single variable. Sets are similar to lists, but they are unordered and do not allow duplicate values. For example, a set of numbers {1, 2, 3} or a set of strings {'apple', 'banana', 'cherry'}.")
        Set: set = {1, 2, 5, False, .69, "Hello", "Hello", True}
        print(f"Example Result: {bold_start}{Set}{end}\n")
        time.sleep(1)

    # Frozen Set
    def FrozenSet():
        print(f"\n{bold_start}Frozen Set Type: -{end}")
        print("Definition: A frozen set is a collection of items that are unordered and unchangeable. Frozen sets are similar to sets, but they are immutable, which means that once a frozen set is created, its elements cannot be changed. For example, a frozen set of numbers {1, 2, 3} or a frozen set of strings {'apple', 'banana', 'cherry'}.")
        MyList = [1, 2, 5, False, .69, "Hello", "Hello", True]
        result = frozenset(MyList)
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    ReadAll = lambda: [Int(), String(), Float(), Boolean(), List(), Dict(), Complex(), Tuple(), Set(), FrozenSet()]

    # Navigation
    read = int(input("In Data types, What you wanna read?\n1. Int\n2. String\n3. Float\n4. Boolean\n5. List\n6. Dictionary\n7. Complex\n8. Tuple\n9. Set\n10. Frozen Set\n11. Read All\n12. Exit\nEnter your choice: "))
    
    while read != 12:
        if read == 1:
            Int()
            read = int(input("In Data types, What you wanna read?\n1. Int\n2. String\n3. Float\n4. Boolean\n5. List\n6. Dictionary\n7. Complex\n8. Tuple\n9. Set\n10. Frozen Set\n11. Read All\n12. Exit\nEnter your choice: "))
        elif read == 2:
            String()
            read = int(input("In Data types, What you wanna read?\n1. Int\n2. String\n3. Float\n4. Boolean\n5. List\n6. Dictionary\n7. Complex\n8. Tuple\n9. Set\n10. Frozen Set\n11. Read All\n12. Exit\nEnter your choice: "))
        elif read == 3:
            Float()
            read = int(input("In Data types, What you wanna read?\n1. Int\n2. String\n3. Float\n4. Boolean\n5. List\n6. Dictionary\n7. Complex\n8. Tuple\n9. Set\n10. Frozen Set\n11. Read All\n12. Exit\nEnter your choice: "))
        elif read == 4:
            Boolean()
            read = int(input("In Data types, What you wanna read?\n1. Int\n2. String\n3. Float\n4. Boolean\n5. List\n6. Dictionary\n7. Complex\n8. Tuple\n9. Set\n10. Frozen Set\n11. Read All\n12. Exit\nEnter your choice: "))
        elif read == 5:
            List()
            read = int(input("In Data types, What you wanna read?\n1. Int\n2. String\n3. Float\n4. Boolean\n5. List\n6. Dictionary\n7. Complex\n8. Tuple\n9. Set\n10. Frozen Set\n11. Read All\n12. Exit\nEnter your choice: "))
        elif read == 6:
            Dict()
            read = int(input("In Data types, What you wanna read?\n1. Int\n2. String\n3. Float\n4. Boolean\n5. List\n6. Dictionary\n7. Complex\n8. Tuple\n9. Set\n10. Frozen Set\n11. Read All\n12. Exit\nEnter your choice: "))
        elif read == 7:
            Complex()
            read = int(input("In Data types, What you wanna read?\n1. Int\n2. String\n3. Float\n4. Boolean\n5. List\n6. Dictionary\n7. Complex\n8. Tuple\n9. Set\n10. Frozen Set\n11. Read All\n12. Exit\nEnter your choice: "))
        elif read == 8:
            Tuple()
            read = int(input("In Data types, What you wanna read?\n1. Int\n2. String\n3. Float\n4. Boolean\n5. List\n6. Dictionary\n7. Complex\n8. Tuple\n9. Set\n10. Frozen Set\n11. Read All\n12. Exit\nEnter your choice: "))
        elif read == 9:
            Set()
            read = int(input("In Data types, What you wanna read?\n1. Int\n2. String\n3. Float\n4. Boolean\n5. List\n6. Dictionary\n7. Complex\n8. Tuple\n9. Set\n10. Frozen Set\n11. Read All\n12. Exit\nEnter your choice: "))
        elif read == 10:
            FrozenSet()
            read = int(input("In Data types, What you wanna read?\n1. Int\n2. String\n3. Float\n4. Boolean\n5. List\n6. Dictionary\n7. Complex\n8. Tuple\n9. Set\n10. Frozen Set\n11. Read All\n12. Exit\nEnter your choice: "))
        elif read == 11:
            ReadAll()
            print(f"\n{bold_start}All Data Types Read Successfully!{end}\n")
            read = int(input("In Data types, What you wanna read?\n1. Int\n2. String\n3. Float\n4. Boolean\n5. List\n6. Dictionary\n7. Complex\n8. Tuple\n9. Set\n10. Frozen Set\n11. Read All\n12. Exit\nEnter your choice: "))
        elif read == 12:
            break
        else:
            print("\nInvalid Input! 🧐\nChoose between 1 to 12.\n")
            time.sleep(1)
            read = int(input("In Data types, What you wanna read?\n1. Int\n2. String\n3. Float\n4. Boolean\n5. List\n6. Dictionary\n7. Complex\n8. Tuple\n9. Set\n10. Frozen Set\n11. Read All\n12. Exit\nEnter your choice: "))