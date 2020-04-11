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










