# There was a set of cards with numbers from 1 to N. One of the card is now lost.
# Determine the number on that lost card given the numbers for the remaining cards.
# Given a number N, followed by N − 1 integers - representing the numbers on the remaining cards (distinct integers in the range from 1 to N).
# Find and print the number on the lost card.
n = int(input())
sumc = 0
for i in range(1, n + 1):
	sumc += i
for i in range(n - 1):
	sumc -= int(input())
print(sumc)

