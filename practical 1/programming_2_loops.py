for i in range(1,21,2):     # Print the odd numbers between the range#
    print(i, end=' ')
print()
for j in range(0,101,9):   #This will print the 10th number in range#
    print(j, end=' ')
print()
for k in range(20,0,-1):   #print numbers from 20 to 0#
    print(k, end=' ')
print()
stars = int(input("Number of stars: "))   #using for loop print stars#
for m in range(1, stars+1):
    print("*", end='')
print()
number_of_stars = int(input("Number of stars: "))
for l in range(1, number_of_stars+1):   # using for loop print stars in different lines#
    print(l*"*")
print()  # Show stars according to order#
