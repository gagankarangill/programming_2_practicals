"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting with the str.format() method
Want to read more about it? https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035
# A better way - using str.format():
print("{} {} for about ${:,.2f}!".format(year, name, cost))

# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(name, cost))

# Aligning columns:
for i in range(0, 180, 50):
    print("{:4}".format(i))


# A version of the above loop using the enumerate function, useful when you want the index and value

# TODO: Use string formatting to produce the output:
# 1922 Gibson L-5 CES for about $16,035!

# TODO: Using a for loop with the range function and string formatting,
# produce the following right-aligned output (do not use a list):
#   0
#  50
# 100
# 150