# CodinGame.com

### Onboarding
```
# game loop
while 1:
    enemy_1 = input()  # name of enemy 1
    dist_1 = int(input())  # distance to enemy 1
    enemy_2 = input()  # name of enemy 2
    dist_2 = int(input())  # distance to enemy 2
    
    # Action code 
    if dist_1 < dist_2:
        print(enemy_1)
    else:
        print(enemy_2)
```

When breaking down into steps this is what the code is doing:
1. Creating inputs for the enemies, as well as their distances
2. Using conditional statement to determine which enemy is closer than the other 

### The Descent 
``` 
import sys
import math

# game loop
while True:
    max = 0
    imax = 0
    for i in range(8):
        mountain_h = int(input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        if mountain_h > max:
            max = mountain_h
            imax = i

    print(imax)
```

This code finds the max of the 8 values that were given as an input, and then determines the largest value. Then it gives out the ouput as the index number of the max value. 


### Power of Thor: Episode 1
```
import sys
import math

light_x, light_y, initial_tx, intial_ty = [int(i) for i in input().split()]
thor_x, thor_y = initial_tx, initial_ty

# game loop
while 1:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    # Direction that Thor needs to move towards
    direction_x = ""
    direction_y = ""
    # Write an action using print
    if thor_x > light_x:
        direction_x = "W"
        thor_x -= 1
    elif thor_x < light_x:
        direction_x = "E"
        thor_x += 1
        
    if thor_y > light_y:
        direction_y = "N"
        thor_y -= 1
    elif thor_y < light_y:
        direction_y = "S"
        thor_y += 1

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(direction_y + direction_x)
```
The steps are the following:
1. Creating inputs for coordinates of light, and the initial coordinate of where Thor starts 
2. Initialize coordinate of Thor as the initial coordinate from the input 
3. Use conditional statement to determine which way the Thor has to move towards 
4. Print the final value of direction

All of the action codes are located inside the infinite loop and this loop allows the code to run infinite times until Thor reaches the goal.

### Comment 

At first the programming was a little confusing because the output was in the game, and so I didn't know how to code, although I gradually got the idea. For the second code I looked fully at the solution. I had the idea of first putting all the inputs in the array, and then finding the max value by using the syntax `max(list)`. Although for some reason, it seemed to not work, thus I ended up using the suggested code found in the solution. I don't quite understand how `if mountain_h > max`, determines the maximum of the mountain_h. For the other code, I understood fully what was going on, and for the last code, after I did several rounds and still didn't work, I peeked at the solution to get a general idea of what the algorithm, or the procedures are, and then finished up the code.


