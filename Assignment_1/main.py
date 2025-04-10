import DataTypes as dt
import SpecialKeywords as sk
import time

# Navigation
read = int(input("What you wanna read?\n1. Data Types\n2. Special Keywords\n3. Exit\nEnter your choice: "))

while read != 3:
    if read == 1:
        dt.Data_Types()
        read = int(input("\nWhat you wanna read?\n1. Data Types\n2. Special Keywords\n3. Exit\nEnter your choice: "))
    elif read == 2:
        sk.Special_Keywords()
        read = int(input("\nWhat you wanna read?\n1. Data Types\n2. Special Keywords\n3. Exit\nEnter your choice: "))
    elif read == 3:
        break
    else:
        print("\nInvalid Input! 🧐\nChoose between 1 to 3.\n")
        time.sleep(1)
        read = int(input("What you wanna read?\n1. Data Types\n2. Special Keywords\n3. Exit\nEnter your choice: "))
# End of the program