# Loops for loop and while loop
# for loop is used to iterate through the data
# Syntax for <variable_name> in <name_of_data>

# shopping_list = ["Eggs", "Milk", "Super Malt"]
# print(shopping_list)

# for items in shopping_list:
#     if items == "Milk":
#         print(items)

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
name = input("What is your name?    ")
age = int(input("How old are you?    "))
birth_year = 2020 - age
already_happened = input("Has your birthday happened this year?   (Y/N)    ")

if already_happened.lower() == "y":
    print("OMG", name, "you are", age, "years old so you were born in the year", birth_year)
else:
    birth_year -= 1
    print("OMG", name, "you are", age, "years old so you were born in the year", birth_year)


# Loop Task

#1)

for i in range(10):
     print("Hello")


#2 and 3

list = []
for i in range(10):
    name = input("What name do you want to input?    ")
    list.append(name)
    continue
print("Your list of names is", list)

list_names_lower = []
for i in list:
    list_names_lower.append(i.lower())
    continue
print(list_names_lower)

#4
number_list = [2,5,6,7,8,9,10]
odds = []
evens = []
for i in number_list:
    if i % 2 != 0:
        odds.append(i)
    else:
        evens.append(i)

print("The odd numbers are", odds)
print("The even numbers are", evens)