# # print("{0} World {1}".format('hi', 'hello'))
#
# # INPUT USAGE
#
# # num = int(input("Enter a number: "))
# # x = (num % 2)
# # if x == 0:
# #     print("is even")
# # else:
# #     print("is odd")
# #
# # print("\n")
# #
# # # INPUT USAGE
# #
# # fruits = ["Apple", "Grapes", "Pineapple", "Guava"]
# #
# # fruits.pop(0)
# #
# # print(fruits)
# #
# # print("\n")
#
# # FUNCTION CALLS
#
#
# def test(numbers):
#     for number in numbers:
#         if number is not None:
#             print("*", end="\n")
#         else:
#             print(end=" ")
#
#
# def main():
#     numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print(test(numbers))
#
#
# main()
# print("\n")
#
# # WHILE LOOP
#
# # x: int = 0
# #
# # while x <= 10:
# #     print("HELLO WORLD!")
# #     x += 1
# #
# # print("\n")
#
# # For Loops
#
# # # PATTERN HALF PYRAMID INVERTED
# for j in range(0, 10):
#     for k in range(0, j + 1):
#         print('*', end=' ')
#     print(' ')
#
# print("\n")
#
#
# # PATTERN HALF PYRAMID
# rows = int(10)
# for i in range(rows, 0, - 1):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")
#
# print("\n")
#
# # PATTERN T
# for row in range(5):
#     for col in range(5):
#         if col == 2 or (row == 0 and col != 2):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()
#
# print("\n")
#
# # PATTERN E
# for row in range(5):
#     for col in range(5):
#         if row == 0 or (row == 2) or (row == 4) or (row == 1 and col == 0) or (row == 3 and col == 0):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()


# day = input("Please enter the day:")
# day1 = "sunday"
# day2 = "monday"
# day3 = "tuesday"
# day4 = "wednesday"
# day5 = "thursday"
# day6 = "friday"
# day7 = "saturday"
# if day == day1:
#     print("Sunday is the first day of the week.")
# elif day == day2:
#     print("Monday is the second day of the week.")
# elif day == day3:
#     print("Tuesday is the third day of the week.")
# elif day == day4:
#     print("Wednesday is the fourth day of the week.")
# elif day == day5:
#     print("Thursday is the fifth day of the week.")
# elif day == day6:
#     print("Friday is the sixth day of the week.")
# elif day == day7:
#     print("Saturday is the seventh day of the week.")

# loop = 1
# while loop == 1:
#     print("1. ADDITION")
#     print("2. SUBTRACTION")
#     print("3. MULTIPLICATION")
#     print("4. DIVISION")
#     print("5. EXIT")
#     var = int(input("SELECT OPTION: "))
#     if var == 1:
#         x = int(input("Please enter a number: "))
#         y = int(input("Please enter another number: "))
#         print(x+y)
#     elif var == 2:
#         x = int(input("Please enter a number: "))
#         y = int(input("Please enter another number: "))
#         print(x-y)
#     elif var == 3:
#         x = int(input("Please enter a number: "))
#         y = int(input("Please enter another number: "))
#         print(x*y)
#     elif var == 4:
#         x = int(input("Please enter a number: "))
#         y = int(input("Please enter another number: "))
#         print(x/y)
#     elif var == 5:
#         exit()
#         break

# loop = 1
# while loop == 1:
#     print("1. COUNT HOW MANY LOWERCASE")
#     print("2. COUNT HOW MANY UPPERCASE")
#     print("3. COUNT HOW MANY SPACE")
#     print("4. EXIT")
#     var = int(input("SELECT OPTION: "))
#     if var == 1:
#         string = input("Please enter a string: ")
#         count = 0
#         for i in string:
#             if i.islower():
#                 count = count + 1
#         print("The number of lowercase characters is:")
#         print(count)
#
#     elif var == 2:
#         string = input("Please enter a string: ")
#         count = 0
#         for i in string:
#             if i.isupper():
#                 count = count + 1
#         print("The number of uppercase characters is:")
#         print(count)
#     elif var == 3:
#         string = input("Please enter a STRING: ")
#         count = 0
#         for i in string:
#             if i.isspace():
#                 count = count + 1
#         print("The number of space is:")
#         print(count)
#     elif var == 4:
#         exit()
#         break

# import random
# import os
#
# def check(x):
#     r = random.randint(1, 20)
#     if r == x:
#         print("\n")
#         print("Matched!")
#         ask()
#     else:
#         os.system('clear')
#         print("\n")
#         print("Did not matched")
#         ask()
#
# def ask():
#     print("\n")
#     choice = input("Do you want to continue playing? (Y)es (N)o: ")
#     if (choice == "y") or (choice == "Y"):
#         start()
#     elif (choice == "n") or (choice == "N"):
#         exit()
#     elif (choice != "y") or (choice != "Y"):
#         os.system('clear')
#         ask()
#
# def start():
#     os.system('clear')
#     try:
#         num = int(input("Please enter your guess number: "))
#         check(num)
#     except ValueError:
#         print("\n")
#         print("Please enter an integer")
#         ask()
#
# start()

# lists = []
#
# for a in range(3):
#     lists.append(input("Enter digit: "))
#     print(lists)

def start():
    items = []
    num = int(input("Please enter the number of range: "))
    for i in range(num):
        word = input("Please enter a word: ")
        if len(word) == 5:
            items.append(word)
    print(items)


start()