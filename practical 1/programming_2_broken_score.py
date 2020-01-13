"""" This program will check different conditions and then display results """
score = float(input("Enter Score:"))
if score > 100:       # Condition for score greater than 100#
    print("Invalid Score")
elif score >= 50:      # Condition for score greater or equal than 50#
    print("Passable")
elif score >= 90:      # Condition for score greater or equal than 90#
    print("Excellent")
elif score < 50:      # Condition for score less than 50#
    print("Bad")
else:                  # Condition for other value like negative numbers#
    print("Invalid Score")
