# Loops for loop and while loop
# for loop is used to iterate through the data
# Syntax for <variable_name> in <name_of_data>
#
# shopping_list = ["Eggs", "Milk", "Super Malt"]
# print(shopping_list)
#
# for items in shopping_list:
#     if items == "Milk":
#         print(items)
#
# for items in shopping_list:
#      if items == "Milk":
#          print(items)
#          break
#
# for items in shopping_list:
#      if items == "Milk":
#          print(items)
#          continue

# Task 1 - calculate year of birth
# name = input("What is your name?    ")
# age = int(input("How old are you?    "))
# birth_year = 2020 - age # calculates the year of birth
# already_happened = input("Has your birthday happened this year?   (Y/N)    ")
#
# if already_happened.lower() == "y": # if the user states their birthday happened this year
#     print("OMG", name, "you are", age, "years old so you were born in the year", birth_year) # print statement
# else:  # otherwise
#     birth_year -= 1 # -1 from birth year
#     print("OMG", name, "you are", age, "years old so you were born in the year", birth_year)


# Loop Task

#1)

for i in range(10): # for a value in the range 10 print "Hello
     print("Hello")


#2 and 3

list = []
for i in range(10):   # for a value in the range 10
    name = input("What name do you want to input?    ") # prompt user for a name
    list.append(name) # adds name to the list
    continue
print("Your list of names is", list) # print the list

list_names_lower = []
for i in list:
    list_names_lower.append(i.lower()) # appends list_names_lower with lower case version of list
    continue
print(list_names_lower)

#4
number_list = [2,5,6,7,8,9,10]
odds = []
evens = []
for i in number_list: # for every number in the list
    if i % 2 != 0: # if there is a remainder when dividing by 2
        odds.append(i) # add the number to the list odds
    else: # otherwise
        evens.append(i) # add the number to the list evens

print("The odd numbers are", odds)
print("The even numbers are", evens)