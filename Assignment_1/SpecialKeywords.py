import time

# ANSI escape codes for styling
bold_start = "\033[1m"
italic_start = "\033[3m"
end = "\033[0m"

# Special Keywords
def Special_Keywords():
    print(f"\n{bold_start}Special Keywords:{end}\n")

    # And Keyword
    def And():
        print(f"\n{bold_start}and: -{end}")
        print("Definition: The and keyword is a logical operator that is used to combine two or more conditions. It returns True if all conditions are True, and False if any condition is False. For example, the expression (x > 5 and x < 10) is True if x is between 5 and 10.")
        x = 7
        result = x > 5 and x < 10
        print(f"Example Result: {bold_start}{result}{end}")
        time.sleep(1)
    
    # As Keyword
    def As():
        print(f"\n{bold_start}as: -{end}")
        print("Definition: The as keyword is used to create an alias for a module or a function. It allows you to import a module or function with a different name. For example, the statement import math as m imports the math module and creates an alias m for it.")
        import math as m

        result = int(m.sqrt(16))
        print(f"Example Result: {bold_start}{result}{end}")
        time.sleep(1)

    # Assert Keyword
    def Assert():
        print(f"\n{bold_start}assert: -{end}")
        print("Definition: The assert keyword is used for debugging purposes. It tests a condition and raises an AssertionError if the condition is False. For example, the statement assert x > 0 checks if x is greater than 0, and raises an error if it is not.")
        x = 5
        assert x > 0, "x should be greater than 0"
        print(f"Example Result: {bold_start}{x}{end}")
        time.sleep(1)

    # Break Keyword
    def Break():
        print(f"\n{bold_start}break: -{end}")
        print("Definition: The break keyword is used to exit a loop prematurely. It breaks out of the current loop and continues with the next statement after the loop. For example, the statement break exits the loop when x is equal to 5.")
        print(f"Example Result:")
        x = 0
        while x < 10:
            if x == 5:
                break
            print(x)
            x += 1
        time.sleep(1)

    # Class Keyword
    def Class():
        print(f"\n{bold_start}class: -{end}")
        print("Definition: The class keyword is used to define a new class. A class is a blueprint for creating objects. It defines the properties and methods that the objects will have. For example, the statement class Dog defines a new class called Dog.")
        class Cat:
            def meow(self):
                return "Meow!"
        cat = Cat()
        print(f"Example Result: {bold_start}{cat.meow()}{end}")
        time.sleep(1)

    # Continue Keyword
    def Continue():
        print(f"\n{bold_start}continue: -{end}")
        print("Definition: The continue keyword is used to skip the current iteration of a loop and continue with the next iteration. For example, the statement continue skips the rest of the loop when x is equal to 5.")
        print(f"Example Result:")
        x = 0
        while x < 10:
            x += 1
            if x == 5:
                continue
            print(x)
        time.sleep(1)

    # Def Keyword
    def Def():
        print(f"\n{bold_start}def: -{end}")
        print("Definition: The def keyword is used to define a new function. A function is a block of code that performs a specific task. For example, the statement def greet() defines a new function called greet.")
        def greet(name):
            return f"Hello, {name}!"
        print(f"Example Result: {bold_start}{greet('Abdul Rehman Jiwani')}{end}")
        time.sleep(1)
    
    # Del Keyword
    def Del():
        print(f"\n{bold_start}del: -{end}")
        print("Definition: The del keyword is used to delete an object. It removes the reference to the object from memory. For example, the statement del x deletes the variable x.")
        x = 5
        print(f"Example Result: {bold_start}{x}{end}")
        del x
        time.sleep(1)

    # Elif Keyword
    def Elif():
        print(f"\n{bold_start}elif: -{end}")
        print("Definition: The elif keyword is used in conditional statements. It stands for 'else if' and allows you to check multiple conditions. For example, the statement if x > 5: print('x is greater than 5') elif x < 5: print('x is less than 5') checks if x is greater than or less than 5.")
        x = 1
        if x > 5:
            result = "x is greater than 5"
        elif x < 5:
            result = "x is less than 5"
        else:
            result = "x is equal to 5"
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # Else Keyword
    def Else():
        print(f"\n{bold_start}else: -{end}")
        print("Definition: The else keyword is used in conditional statements. It specifies a block of code that will be executed if the condition is False. For example, the statement if x > 5: print('x is greater than 5') else: print('x is less than or equal to 5') checks if x is greater than 5.")
        x = 5
        if x > 5:
            result = "x is greater than 5"
        elif x < 5:
            result = "x is less than 5"
        else:
            result = "x is equal to 5"
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # Except Keyword
    def Except():
        print(f"\n{bold_start}except: -{end}")
        print("Definition: The except keyword is used with exceptions. It specifies a block of code that will be executed if an exception occurs. For example, the statement try: x = 1 / 0 except ZeroDivisionError: print('Cannot divide by zero') checks for a division by zero error.")
        try:
            x = 5 / 0
        except ZeroDivisionError:
            result = "Cannot divide by zero"
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # False Keyword
    def false():
        print(f"\n{bold_start}False: -{end}")
        print("Definition: The False keyword is a boolean value that represents the result of a comparison operation that is not true. For example, the statement x = 5 < 3 assigns the value False to x.")
        x = 5 < 3
        print(f"Example Result: {bold_start}{x}{end}\n")
        time.sleep(1)

    # Finally Keyword
    def Finally():
        print(f"\n{bold_start}finally: -{end}")
        print("Definition: The finally keyword is used with exceptions to define a block of code that will be executed no matter whether an exception occurs or not. It is often used to clean up resources, such as closing files or releasing locks. For example, the statement try: x = 1 / 0 finally: print('This will always execute') ensures that the finally block is executed even if an exception occurs.")
        print(f"Example Result:")
        try:
            x = 5 / 0
        except ZeroDivisionError:
            print("Cannot divide by zero")
        finally:
            print("This will always execute")
        time.sleep(1)

    # For Keyword
    def For():
        print(f"\n{bold_start}for: -{end}")
        print("Definition: The for keyword is used to create a for loop. A for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects. For example, the statement for x in range(5): print(x) prints the numbers 0 to 4.")
        print(f"Example Result:")
        for x in range(6):
            print(x)
        time.sleep(1)

    # From Keyword
    def From():
        print(f"\n{bold_start}from: -{end}")
        print("Definition: The from keyword is used to import specific parts of a module. It allows you to import only the parts of a module that you need, rather than importing the entire module. For example, the statement from math import sqrt imports only the sqrt function from the math module.")
        from math import sqrt
        result = int(sqrt(16))
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # Global Keyword
    def Global():
        print(f"\n{bold_start}global: -{end}")
        print("Definition: The global keyword is used to declare a global variable. A global variable is a variable that can be accessed from anywhere in the program, including inside functions. For example, the statement global x declares x as a global variable.")
        x = 5
        def set_global_x(value):
            global x
            x = value
        set_global_x(10)
        print(f"Example Result: {bold_start}{x}{end}\n")
        time.sleep(1)

    # If Keyword
    def If():
        print(f"\n{bold_start}if: -{end}")
        print("Definition: The if keyword is used to create a conditional statement. It allows you to execute a block of code only if a certain condition is True. For example, the statement if x > 5: print('x is greater than 5') checks if x is greater than 5.")
        x = 10
        if x > 5:
            result = "x is greater than 5"
        elif x < 5:
            result = "x is less than 5"
        else:
            result = "x is equal to 5"
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # Import Keyword
    def Import():
        print(f"\n{bold_start}import: -{end}")
        print("Definition: The import keyword is used to import a module. A module is a file that contains Python code, such as functions and classes. For example, the statement import math imports the math module.")
        import math

        result = int(math.sqrt(25))
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # In Keyword
    def In():
        print(f"\n{bold_start}in: -{end}")
        print("Definition: The in keyword is used to check if a value is present in a sequence (such as a list, tuple, or string) or other iterable objects. It returns True if the value is found, and False otherwise. For example, the statement x in [1, 2, 3] checks if x is present in the list.")
        x = 10
        my_list = [1, 2, 3, 4, 5]
        result = x in my_list
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # Is Keyword
    def Is():
        print(f"\n{bold_start}is: -{end}")
        print("Definition: The is keyword is used to test if two variables are equal. It checks if both variables point to the same object in memory. For example, the statement x is y checks if x and y are the same object.")
        x = [1, 2, 3]
        y = x
        result = x is y
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # Lambda Keyword
    def Lambda():
        print(f"\n{bold_start}lambda: -{end}")
        print("Definition: The lambda keyword is used to create an anonymous function. An anonymous function is a function that does not have a name. It is often used for short, throwaway functions that are not reused elsewhere in the code. For example, the statement lambda x: x * 2 creates an anonymous function that doubles its input.")
        double = lambda x: x * 2
        print(f"Example Result: {bold_start}{double(5)}{end}\n")
        time.sleep(1)

    # None Keyword
    def none():
        print(f"\n{bold_start}None: -{end}")
        print("Definition: The None keyword represents a null value. It is used to indicate that a variable does not have a value or that a function does not return a value. For example, the statement x = None assigns the value None to x.")
        x = None
        print(f"Example Result: {bold_start}{x}{end}\n")
        time.sleep(1)

    # NonLocal Keyword
    def NonLocal():
        print(f"\n{bold_start}nonlocal: -{end}")
        print("Definition: The nonlocal keyword is used to declare a non-local variable. A non-local variable is a variable that is not defined in the current scope, but in an outer (enclosing) scope. For example, the statement nonlocal x declares x as a non-local variable.")
        # x = 5
        def outer_function():
            x = 10
            def inner_function():
                x = 20
                def inner_inner_function():
                    nonlocal x
                    x += 5
                    return x
                return inner_inner_function()
            return inner_function()
        result = outer_function()
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # Not Keyword
    def Not():
        print(f"\n{bold_start}not: -{end}")
        print("Definition: The not keyword is a logical operator that negates a condition. It returns True if the condition is False, and False if the condition is True. For example, the statement not (x > 5) returns True if x is less than or equal to 5.")
        x = 5
        result = not (x > 5)
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # Or Keyword
    def Or():
        print(f"\n{bold_start}or: -{end}")
        print("Definition: The or keyword is a logical operator that is used to combine two or more conditions. It returns True if at least one condition is True, and False if all conditions are False. For example, the expression (x > 5 or x < 10) is True if x is greater than 5 or less than 10.")
        x = 5
        result = x > 10 or x < 5
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # Pass Keyword
    def Pass():
        print(f"\n{bold_start}pass: -{end}")
        print("Definition: The pass keyword is a null statement. It is used as a placeholder for future code. It does nothing when executed. For example, the statement pass is often used in empty functions or classes.")

        def empty_function():
            pass
        print(f"Example Result: {bold_start}{empty_function()}{end}\n")
        time.sleep(1)

    # Raise Keyword
    def Raise():
        print(f"\n{bold_start}raise: -{end}")
        print("Definition: The raise keyword is used to raise an exception. It allows you to create custom exceptions and handle errors in your code. For example, the statement raise ValueError('Invalid value') raises a ValueError exception with the specified message.")
        try:
            raise ValueError("Invalid value")
        except ValueError as e:
            result = str(e)
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # Return Keyword
    def Return():
        print(f"\n{bold_start}return: -{end}")
        print("Definition: The return keyword is used to exit a function and return a value. It allows you to send a value back to the caller of the function. For example, the statement return x returns the value of x from the function.")
        def add(a, b):
            return a + b
        result = add(34, 16)
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # True Keyword
    def true():
        print(f"\n{bold_start}True: -{end}")
        print("Definition: The True keyword is a boolean value that represents the result of a comparison operation that is true. For example, the statement x = 5 > 3 assigns the value True to x.")
        x = 5 > 3
        print(f"Example Result: {bold_start}{x}{end}\n")
        time.sleep(1)

    # Try Keyword
    def Try():
        print(f"\n{bold_start}try: -{end}")
        print("Definition: The try keyword is used to create a try...except statement. It allows you to handle exceptions that may occur in your code. For example, the statement try: x = 1 / 0 except ZeroDivisionError: print('Cannot divide by zero') checks for a division by zero error.")
        try:
            x = 5 / 0
        except ZeroDivisionError:
            result = "Cannot divide by zero"
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # While Keyword
    def While():
        print(f"\n{bold_start}while: -{end}")
        print("Definition: The while keyword is used to create a while loop. A while loop is used to execute a block of code as long as a certain condition is True. For example, the statement while x < 5: print(x) prints the numbers 0 to 4.")
        print(f"Example Result:")
        x = 1
        while x <= 5:
            print(x)
            x += 1
        time.sleep(1)

    # With Keyword
    def With():
        print(f"\n{bold_start}with: -{end}")
        print("Definition: The with keyword is used to simplify exception handling. It is often used when working with files or other resources that need to be cleaned up after use. For example, the statement with open('file.txt', 'r') as f: reads the file and automatically closes it after use.")
        with open("test.txt", "w") as file:
            file.write("Hello, World!")
        print(f"Example Result: {bold_start}File written successfully!{end}\n")
        time.sleep(1)

    # Yield Keyword
    def Yield():
        print(f"\n{bold_start}yield: -{end}")
        print("Definition: The yield keyword is used to return a list of values from a generator. A generator is a special type of iterator that generates values on the fly. For example, the statement yield x returns the value of x from the generator.")
        print("Example Result:")
        def generate_numbers(n):
            for i in range(n):
                yield i
        for num in generate_numbers(5):
            print(num)
        time.sleep(1)
    
    # Match Keyword
    def Match():
        print(f"\n{bold_start}match: -{end}")
        print("Definition: The match keyword is used to perform pattern matching. It allows you to match a value against a series of patterns and execute the corresponding block of code. For example, the statement match x: case 1: print('x is 1') matches the value of x against the specified patterns.")
        print("Example Result:")
        def match_example(x):
            match x:
                case 1:
                    return "x is 1"
                case 2:
                    return "x is 2"
                case _:
                    return "x is something else"
        result = match_example(2)
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)
    
    # Case Keyword
    def Case():
        print(f"\n{bold_start}case: -{end}")
        print("Definition: The case keyword is used in pattern matching. It allows you to specify a pattern to match against a value. For example, the statement case 1: print('x is 1') matches the value of x against the specified pattern.")
        print("Example Result:")
        def match_example(x):
            match x:
                case 1:
                    return "x is 1"
                case 2:
                    return "x is 2"
                case _:
                    return "x is something else"
        result = match_example(1)
        print(f"Example Result: {bold_start}{result}{end}\n")
        time.sleep(1)

    # Async Keyword
    def Async():
        print(f"\n{bold_start}async: -{end}")
        print("Definition: The async keyword is used to define an asynchronous function, or coroutine. It allows you to write asynchronous code that can run concurrently with other code. For example, the statement async def my_coroutine() defines a new asynchronous function.")
        print("Example Result:")
        import asyncio

        # An async function that simulates a long-running task
        async def fetch_data():
            print("Fetching data...")
            await asyncio.sleep(2)  # Simulating a delay of 2 seconds
            print("Data fetched!\n")

        # Another async function that simulates processing data
        async def process_data():
            print("Processing data...")
            await asyncio.sleep(1)  # Simulating a shorter delay of 1 second
            print("Data processed!")

        # Main function that runs both coroutines
        async def main():
            # We can run these two async functions concurrently using asyncio.gather
            await asyncio.gather(fetch_data(), process_data())

        # Running the main coroutine
        asyncio.run(main())
        time.sleep(1)

    # Await Keyword
    def Await():
        print(f"\n{bold_start}await: -{end}")
        print("Definition: The await keyword is used in asynchronous functions to specify a point in the function where control is given back to the event loop for other functions to run. For example, the statement await my_coroutine() calls the asynchronous function and waits for it to complete.")
        print("Example Result:")
        import asyncio

        # Simulating a delay with asyncio.sleep
        async def delay(seconds):
            print(f"Waiting for {seconds} seconds...")
            await asyncio.sleep(seconds)
            print(f"Waited for {seconds} seconds!")

        async def main():
            print("Start fetching data...")
            
            # Await the delay coroutine, this pauses the execution of the main function until the delay is done
            await delay(2)  # Waits for 2 seconds
            
            print("Data fetched after 2 seconds!\n")

        # Running the event loop to execute the main coroutine
        asyncio.run(main())
        time.sleep(1)

    # Read All
    ReadAll = lambda : [And(), As(), Assert(), Break(), Class(), Continue(), Def(), Del(), Elif(), Else(), Except(), false(), Finally(), For(), From(), Global(), If(), Import(), In(), Is(), Lambda(), none(), NonLocal(), Not(), Or(), Pass(), Raise(), Return(), true(), Try(), While(), With(), Yield(), Match(), Case(), Async(), Await()]

    # --------------------------------------------------------------------------------------
    
    # Navigation Starts...
    read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))

    while read != 39:
        if read == 1:
            And()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 2:
            As()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 3:
            Assert()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 4:
            Break()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 5:
            Class()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 6:
            Continue()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 7:
            Def()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 8:
            Del()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 9:
            Elif()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 10:
            Else()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 11:
            Except()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 12:
            false()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 13:
            Finally()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 14:
            For()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 15:
            From()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 16:
            Global()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 17:
            If()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 18:
            Import()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 19:
            In()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 20:
            Is()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 21:
            Lambda()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 22:
            none()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 23:
            NonLocal()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 24:
            Not()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 25:
            Or()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 26:
            Pass()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 27:
            Raise()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 28:
            Return()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 29:
            true()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 30:
            Try()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 31:
            While()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 32:
            With()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 33:
            Yield()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 34:
            Match()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 35:
            Case()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 36:
            Async()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 37:
            Await()
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All\n39. Exit!\nEnter your choice: "))
        elif read == 38:
            ReadAll()
            time.sleep(2)
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All!\n39. Exit!\nEnter your choice: "))
        elif read == 39:
            break
        else:
            print("\nInvalid Input! 🧐\nChoose between 1 to 37.\n")
            time.sleep(2)
            read = int(input("What you wanna read?\n1. and keyword\n2. as keyword\n3. assert keyword\n4. break keyword\n5. class keyword\n6. continue keyword\n7. def keyword\n8. del keyword\n9. elif keyword\n10. else keyword\n11. except keyword\n12. False keyword\n13. finally keyword\n14. for keyword\n15. from keyword\n16. global keyword\n17. if keyword\n18. import keyword\n19. in keyword\n20. is keyword\n21. lambda keyword\n22. None keyword\n23. nonlocal keyword\n24. not keyword\n25. or keyword\n26. pass keyword\n27. raise keyword\n28. return keyword\n29. True keyword\n30. try keyword\n31. while keyword\n32. with keyword\n33. yield keyword\n34. match keyword\n35. case keyword\n36. async keyword\n37. await keyword\n38. Read All!\n39. Exit!\nEnter your choice: "))