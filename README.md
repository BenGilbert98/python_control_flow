# Control Flow
## if, elif and else statements
- If is used to perform an action if a condition is true
- Elif is else if
- Else is used to perform an action if none of the if statements are used
- Syntax : if then condition
- example:
```
 age = int(input("How old are you?"))  # promts the user to enter an age and converts it to integer

 if age >= 15:
     print("You are 15 or above")
 elif age < 15:
     print("You can't watch the movie you are too young")
 else:
     print("Oops something went wrong ... try again")
```
- Create a program using control flow with if, elif and else using operators
- Check age restrictions before selling the ticket (18, 15, 12, PG, U)
- else block should ensure to display message if other conditions do not match
```
age = int(input("Please enter your age    "))


if age >= 18:
    print("You can watch any film")
if age in range (15,17):   # checks if age is in the range 15-17
    print("You can watch everything but an 18 film")
if age in range (12,14):
    print("You can watch everything but 15 and 18 rated films")
if age in range (3,11):
    print("You can watch everything but 12,15 and 18 rated films")
elif age < 3:
    print("You can only watch PG and U rated films")
```
# For and While loops
## For Loops
- for loops are used to iterate through data
- ```break``` and ```continue``` can be used to control flow
Loops for loop and while loop
-for loop is used to iterate through the data
-Syntax for <variable_name> in <name_of_data>
-Examples:
``` 
shopping_list = ["Eggs", "Milk", "Super Malt"] # Creates a list
print(shopping_list)

for items in shopping_list:  # iterates through list at each item
    if items == "Milk":
        print(items)

for items in shopping_list:
     if items == "Milk":
         print(items)
         break  # break statement

for items in shopping_list:
     if items == "Milk":
         print(items)
         continue
```
## While Loops
- is not regularly used however it is mainly used for monitoring
- We can use ```break``` and ```continue``` to help control the flow of our loop
- example (Lets create a while loop)
break and continue are keywords that we can use to control the flow of our program
Syntax while <variable> <condition> <value>:)
```
number = 0

while number < 10:
    print(f"it's working -> {number}")
    if number == 5:
        break
    number += 1
```
- example (taking user input with while loop)
```
user_prompt = True

while user_prompt:
    age = input("Please enter your age    ")
    # Note this user input is within our while loop therefore it will prompt the user until we get desired input
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("Please provide age in digits")

print(f"Your age is {age}")
``` 