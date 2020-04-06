# Write a program that accepts a comma separated sequence of words as input
# and prints the words in a comma-separated sequence after sorting them alphabetically.

str = input()
splstr = str.split(",")
final = sorted(splstr)
print(final)
