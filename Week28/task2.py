# With a given integral number n, write a program to generate a dictionary that contains (i, i*i),
# such that i is an integral number between 1 and n (both included).
# The program should print the dictionary.

n = int(input("Enter max number here: "))
x = dict()
for i in range(1, n+1):
    x[f'{i}'] = i**2
print(x)
