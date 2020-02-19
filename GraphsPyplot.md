# Using matplotlib

### 1. Generate 1000 random numbers between 1 and 100. Create a graph for this numbers where the x axis are the numbers 1 to 1000, and the y axis are the random numbers.

1. import necessary libraries 
2. generate 1000 random numbers from 1 to 100 using randomint
3. calculate the average then print it on the console 
4. set x and y for the graph
5 show the graph 

```
# ① 　Generate 1000 random numbers between 1 and 100.
# Create a graph for this numbers where the x axis are the numbers 1 to 1000, and the y axis are the random numbers.
from numpy.random import randint
import matplotlib.pyplot as plt
# generate 1000 random numbers from 1 to 100
randNum = randint(1, 100, 1000)
print(randNum)

# create the value for the x variable from 1 to 1000
x = [i for i in range(0, 1000)]
# do the same for y but with the random numbers generated
y = randNum

# create graph
plt.plot(x, y)
# title for the axis
plt.xlabel('x')
plt.ylabel('y')
# show the graph
plt.show()
```
I had some difficulties while developing this program. First of all, I had difficulties importing matplotlib, since I did not have it in first place. I tried isntalling through terminal although this didn't also work, so I decided to intall the matplotlib in the pycharm. Also when setting the y values of the graph, it values had to be in a list, therefore I used `from numpy.random import randint` so that when generating random number, it automatically put every value generated inside a list. I got this code from Machine Learning Mastery[1]. There are also different ways of adding values in the list such as appending all the 1000 values into a list, although this looked shorter, therefore I used this code. The final graph I got can be found in [resourcePyplot](#resourcePyplot).

### 2. Calculate the average of the 1000 random numbers in ① using a loop.

1. create variable "sum" and intialize it as 0
3. run a for loop for len(randNum) times
4. in the for loop add all the values to variable sum
5. divide sum by the number of values
6. print the sum

```
# ②　 Calculate the average of the 1000 random numbers in ① using a loop.
sum = 0
for num in randNum:
    sum += num
avg = sum / len(randNum)
print(avg)
```

The randNum is from task 1. The random number generated in question 1, is directly used in this second question to calculate the average. The variable sum had to initialized because it is used in the for loop. `sum += num`, is equivalent as `sum = sum + num`. What this line is doing is that it updates the value of the sum, everytime a new random number generated, is being added. The variable "avg", does not have to be initialized, and we can set it as sum divided by the number of random numbers by default, because there is no need for updating. This gives us the average of the 1000 random numbers: 

```
[33 77 82 59 45 88 68 87 27 78 26 46 43 49 15 22 64 97 65 16 58 12 87 95
 28 55  2 19 26 36  3 48 32  3 44 56 12 78 32 96 61 30 29 82 33 91 11 82
 10 71 29 50 41 44 70 72  2 47 85  8 36 25 66 84 68 92 24 98 35  5 27 63
  7 17 67 69 10 95  7 61 72 52 98 16  8 93 20 59 83 98 77 91 55 73  7 71
 65 70  2 74 15 92 70 50 94 11 47 38 31 12  1 21 43 57 43 82 55 35 37  6
  2 95 74 99 42 65 59 88 57 81 33 44 24 44 57  5 53 77 74 29  1  3 17 84
 61 57 22 16 56 88  4 77 57 72 12 30 94 58 18 94 99 27 98 69 48 81 77 73
 15 84 31 78 97 18 69 99 67 88 82 33 71 13 56 23 34 71 86 59 34 77 50 45
 97 25 83 39 90 86 61 10 21 20 92  6 10 92  4 22 87 41 58 45 96 49 45 40
 47 20 36 99 45 99  1 41 20 47 46 71 31 58 81 41 27 67 26 45 59 27 73 11
 67 95 49 32 14 63 14 35 34  3 23 64 22 46  3 52 26 98 83 63 87 34 56 89
 16 77 88  3 25 83 98 97 62 97 55  5  8 45 53 28 72 65 39 81 58  1  2 90
  1 76 36 80 25 28 98 79 88  2  9 66 93 18 67 84 57 98 40 79 79 18  9 69
 58 16 59  5 75 91 10 60 51 20 31 58 62 62 46 79 41 57 14 77 27 98 51 65
 34 44 92 46 41 42 34 31  1 28 81 86 78 97 55 13 96 25 79 22 34 95 34 70
 61 52 15 37 16 88 21 15 75 75  9 33 20 79 35 45 98 33  8 25 95 71  3 64
 57 18 58 90 19 27 12 79 44  6 62  1 93 16 19 64 28 34 34 36 29 57 83 97
 68 11 33 94 61 64 53 26 77 83 51 49 59 81 81 28 94 23 88 35 42 91 54 41
 24 72 94 12 11 25 67 33 97  1 94 72 40 95  2 33 40 68  1 26  3 26  4 55
 85 43 61 26 45  7 17 91 89 22 50 45 10 40 68 82 77 46 35 13 98  9 49 75
 95 33 51 78 48 23 78  9 15 85  6 68 11 21 82 28 73 43 80 63 93 64 12 23
 27 60 82 61 16 79 97 37 12 39  6 68 44 87 41 56 79 56 82 32 71 92 15 24
 79 70 80 61 74 75 60 77 34 97 53 22 15 91 52 33 63  5 78 58  8 47 99 88
 64 35 60 78 66 81 14 63  3 14 33 22 46 81 45 72 24 93 40 31 82 85  8 65
 37 18 37 76 18  3 17 97 17 39  9 13 16 44 98 77 22 88 51  8  2 33 18 21
 83 35 45 19 19  3 58 57 92 58  1 32 42 43 29 11 49 92 40 65 69 66 17 83
 19 32 71 95 72 65 91 91 36 85 32 37 94  8 25 29 71 20 81 26 85 48 53 97
  9  1 12 82 38 16 93  8 78 98 17 26  8 75 47 20 15  9 29 72  8 62 13 78
 39 23 71 88 21 22 71 46 89  7 90 90 76 84 97 53 12 68 72 27 53 89 70  6
 32 21 80 79 55  8 26  6 10 34 17 39 64 28 80 82 90 21 85 40 97 81  4 29
 28 88 49 51 41 93 60 76 77 15 57 97 19 99 20  7  6 81 98 95 70 30 70 49
 38  2 14 49 77 47 40 66 91 23 91 55  5 25 46 36 24 74  6 50 63 14 94  8
 62 80 37 11 93 94  3 32 95 53 72 39 92  7 90 26 65 58 21 82 73 75  6 48
 17  1 22 65 79 58 90 26 73 51 95 38 59 48 32 53 36  7 97 20 95  1 39 16
 94 79 48 74 37 85 76 23 54 86 43 89 67 25 28 27 23 70 12 48 47 67 91 69
 33 90 12 18 70 39 81 71 35 84 85 80 82 59 35 48 62 79 59 61 42 61  7 23
 83  1 73 77 41 54 80 33 10 30 94  6  9 71 47 24 32 65 88 58 48 73 65 73
 14 81 53 33 40 43 52 39 17 13 97 30 53 15 45  3 82 12 70 78 23 35 48 23
 12 96  5 77 85 83 58 28 96 26 51 34 73 65 59 21 93 93  7 52 92 79 80 35
 10 74 89 64 16 42 64 93 75 36 25 34 91 65 25 24 97 90 55 44 54 98 59 70
 47 64 80 69 96  2 95 26 97 22 54 18 50 51 73 27 75 55  8 19 43 64 35 93
 50 61 18 86  8 40 67 56 29 90 51 83 33 65 88 40]
The average of all the random numbers generated: 50.485
```

### 3. Graph the equation for the wave function 14*sin(0.5*x) in the range x = [-10, 10] with steps of 0.1.

1. import matplotlib
2. define max and min for the x value 
3. create list for x and y 
4. append value (min + 0.1(i + 1)) to set the intervals for x to 0.1
5. append value (14*sin(0.5*x)) for y 
6. give x and y axes titles
7. show graph 

``` 
# ③ 　Graph the equation for the wave function 14*sin(0.5*x) in the range x = [-10, 10] with steps of 0.1.
import matplotlib.pyplot as plt
import numpy as np
import math

# create the value for the x variable from 1 to 1000
max = 10
min = -10
# x = [i for i in range(min, max)]
# # do the same for y but with the random numbers generated
# y = [14 * math.sin(0.5*i) for i in x]
x = []
y = []
# setting the intervals to 0.1
for i in range(200):
    x.append(min + 0.1*(i+1))
    y.append(14 * math.sin(0.5 * x[i]))

# create graph
plt.plot(x, y)
# title for the axis
plt.xlabel('x')
plt.ylabel('y')
# show the graph
plt.show()
```

For the for loop the range 200 was calculated by ((max - min) / 0.1). This equation calculates how many intervals there would be if the numbers were to have a 0.1 increment. In this specific case the maximum and minimum is 10 and -10, thus the calculation would be (10 + 10) / 0.1 = 20 / 0.1 = 200. The rest of the code is basically the same as the first question. The output of this program is also recorded in the resourcePyplot folder in the repo. 

### 4. Create the graph on any other mathematical function you know. 
```
# Creating tan graph
import matplotlib.pyplot as plt
import numpy as np
import math

# set x value range
x = [i for i in range(-10, 10)]
# set y
y = [math.tan(0.5*i) for i in x]

# create graph
plt.plot(x, y)
# title for the axis
plt.xlabel('x')
plt.ylabel('y')
# show the graph
plt.show()
```

The steps are fundamentally the same as the third question, although for this graph, I didn't set the intervals to 0.1 and just left as default. This program also produces an interesting graph, that would also be able in the resourcePyplot folder.



