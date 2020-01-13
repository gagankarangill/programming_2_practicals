# 1st program#
in_file = open("name.txt", "w")
name = input("Please enter your name: ")
print(in_file.write(name))
in_file.close


# 2nd program#
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

# using with
with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
print("your name is", name)


# 3rd program
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)


# sum of numbers
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)

