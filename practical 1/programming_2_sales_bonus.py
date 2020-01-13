""""This program will calculate the bonus value of sales"""
sales = float(input("Enter your sales: $"))
while sales < 0:           # While loop will check negative value#
    sales = float(input("wrong value \nEnter the salary again: $"))
if sales < 1000:           # Calculate bonus for values less than 1000#
    bonus = 0.1*sales
    print("Your bonus is", bonus, "$")
else:                      # Calculate bonus for values greater than or equal to 1000#
    bonus = 15/100*sales
    print("Your bonus is", bonus, "$")
# This program will calculate bonus by checking conditions#
