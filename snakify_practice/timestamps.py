# A timestamp is three numbers: a number of hours, minutes and seconds.
# Given two timestamps, calculate how many seconds is between them.
# The moment of the first timestamp occurred before the moment of the second timestamp

h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
timeInSec1 = (h1 * 3600 + m1 * 60 + s1)
timeInSec2 = (h2 * 3600 + m2 * 60 + s2)
print(timeInSec2 - timeInSec1)