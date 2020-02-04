# Given the integer N - the number of minutes that is passed since midnight
# how many hours and minutes are displayed on the 24h digital clock?
n = int(input())
hour = int((n / 60))
minute = int((n - 60 * hour))
print(hour, "  ", minute)