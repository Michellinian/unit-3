# Chess rook moves horizontally or vertically.
# Given two different cells of the chessboard
# determine whether a rook can go from the first cell to the second in one move.
r1 = int(input())
c1 = int(input())
r2 = int(input())
c2 = int(input())
if r1 == r2 or c1 == c2:
    print("YES")
else:
    print("NO")
