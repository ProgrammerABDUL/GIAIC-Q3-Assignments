# Importing Operators
import AirthmeticOperators as AO
import ComparisonOperators as CO
import LogicalOperators as LO
import BitwiseOperators as BO
import AssignmentOperators as AO2
import IdentityOperators as IO
import MembershipOperators as MO

# Formatting
bold_start = "\033[1m"
itatlic_start = "\033[3m"
end = "\033[0m"

# Heading
print(f"{bold_start}Assignment 2 — Operators in Python{end}\n")

# Navigation
Operators = int(input("Which example you wanna check?\n1. Airthmetic Operators\n2. Comparison Operators\n3. Logical Operators\n4. Bitwise Operators\n5. Assignment Operators\n6. Identity Operators\n7. Membership Operators\n8. Exit\nEnter your choice: "))

while Operators != 8:
    if Operators == 1:
        AO.Airthmetic_Operators(10, 5)
        Operators = int(input("Which example you wanna check?\n1. Airthmetic Operators\n2. Comparison Operators\n3. Logical Operators\n4. Bitwise Operators\n5. Assignment Operators\n6. Identity Operators\n7. Membership Operators\n8. Exit\nEnter your choice: "))
    elif Operators == 2:
        CO.Comparison_Operators(18, 2)
        Operators = int(input("Which example you wanna check?\n1. Airthmetic Operators\n2. Comparison Operators\n3. Logical Operators\n4. Bitwise Operators\n5. Assignment Operators\n6. Identity Operators\n7. Membership Operators\n8. Exit\nEnter your choice: "))
    elif Operators == 3:
        LO.Logical_Operators(9, 4)
        Operators = int(input("Which example you wanna check?\n1. Airthmetic Operators\n2. Comparison Operators\n3. Logical Operators\n4. Bitwise Operators\n5. Assignment Operators\n6. Identity Operators\n7. Membership Operators\n8. Exit\nEnter your choice: "))
    elif Operators == 4:
        BO.Bitwise_Operators(19, 1)
        Operators = int(input("Which example you wanna check?\n1. Airthmetic Operators\n2. Comparison Operators\n3. Logical Operators\n4. Bitwise Operators\n5. Assignment Operators\n6. Identity Operators\n7. Membership Operators\n8. Exit\nEnter your choice: "))
    elif Operators == 5:
        AO2.Assignment_Operators(7, 5)
        Operators = int(input("Which example you wanna check?\n1. Airthmetic Operators\n2. Comparison Operators\n3. Logical Operators\n4. Bitwise Operators\n5. Assignment Operators\n6. Identity Operators\n7. Membership Operators\n8. Exit\nEnter your choice: "))
    elif Operators == 6:
        IO.Identity_Operators()
        Operators = int(input("Which example you wanna check?\n1. Airthmetic Operators\n2. Comparison Operators\n3. Logical Operators\n4. Bitwise Operators\n5. Assignment Operators\n6. Identity Operators\n7. Membership Operators\n8. Exit\nEnter your choice: "))
    elif Operators == 7:
        MO.Membership_Operators()
        Operators = int(input("Which example you wanna check?\n1. Airthmetic Operators\n2. Comparison Operators\n3. Logical Operators\n4. Bitwise Operators\n5. Assignment Operators\n6. Identity Operators\n7. Membership Operators\n8. Exit\nEnter your choice: "))
    elif Operators == 8:
        break
    else:
        print("\nInvalid Input!")
        print("Choose between 1 to 8")
        Operators = int(input("\nWhich example you wanna check?\n1. Airthmetic Operators\n2. Comparison Operators\n3. Logical Operators\n4. Bitwise Operators\n5. Assignment Operators\n6. Identity Operators\n7. Membership Operators\n8. Exit\nEnter your choice: "))