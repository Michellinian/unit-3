# Write a Python program that asks the user for his first name and last name and a number (1, 100].
# The output is a text file with as email addresses for the user:

firstName = input("Enter your first name here: ")
lastName = input("Enter your last name here: ")
usrnum = int(input("Enter a number between 1 to 100: "))

for i in range(1, usrnum+1):
    print(f"{firstName}.{lastName}{i}@uwcisak.jp")
