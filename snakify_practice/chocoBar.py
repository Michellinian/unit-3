# Chocolate bar has the form of a rectangle divided into n×m portions.
# Chocolate bar can be split into two rectangular parts by breaking it along a selected straight line on its pattern.
# Determine whether it is possible to split it so that one of the parts will have exactly k squares.
n = int(input())
m = int(input())
k = int(input())
lim = n * m
if k <= lim:
    if k % n == 0 or k % m == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
