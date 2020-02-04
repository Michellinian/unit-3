# For the given integer X print 1 if it's positive
# -1 if it's negative
# 0 if it's equal to zero
num = int(input())
if num < 0:
    print(-1)
elif num == 0:
    print(0)
else:
    print(1)