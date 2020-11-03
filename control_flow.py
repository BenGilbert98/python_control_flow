# control flow

# if statements
# Syntax : if then condition

# age = int(input("How old are you?"))
#
# if age >= 15:
#     print("You are 15 or above")
# elif age < 15:
#     print("You can't watch the movie you are too young")
# else:
#     print("Oops something went wrong ... try again")

# Create a program using control flow with if, elif and else using operators
# Check age restrictions before selling the ticket
# 18, 15, 12, PG, U
# else block should ensure to display message if other conditions do not match

age = int(input("Please enter your age    "))


if age >= 18:
    print("You can watch any film")
if age in range (15,17):
    print("You can watch everything but an 18 film")
if age in range (12,14):
    print("You can watch everything but 15 and 18 rated films")
if age in range (3,11):
    print("You can watch everything but 12,15 and 18 rated films")
elif age < 3:
    print("You can only watch PG and U rated films")