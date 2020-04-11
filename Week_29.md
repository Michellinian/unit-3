## Question 1 code
```
# Write a Python program that asks the user for his first name and last name and a number (1, 100].
# The output is a text file with as email addresses for the user:

firstName = input("Enter your first name here: ")
lastName = input("Enter your last name here: ")
usrnum = int(input("Enter a number between 1 to 100: "))

for i in range(1, usrnum+1):
    print(f"{firstName}.{lastName}{i}@uwcisak.jp")
```

## Question 2 code
```
# Write a Python program that generates random passwords of length 20.
# The user provides how many passwords should be generated
import string, random

usrinput = int(input())

lett = string.ascii_letters
num = string.digits
punct = string.punctuation
allchar = lett + num + punct

for x in range(1, usrinput+1):
    pwd = ''
    for y in range(20):
        pwd += random.choice(allchar)
    print(f"Password {x}: {pwd}")

```
