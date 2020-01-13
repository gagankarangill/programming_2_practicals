"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Invalid output")
        print("Cannot divide by zero!")
        denominator = int(input("please enter the  value of denominator again : "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Value error is an error that we get because of storing values like we want to convert from string to integer like "21" to 21 but we can't convert "dog" into integer so we will get value error
# we will get zero division error when we get any exception in our code or number will be divided by 0
