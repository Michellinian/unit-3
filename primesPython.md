Prime number in Python 
====

The following programs will check is the numbers are prime numbers or not. 
There are three functions in this "Prime" program, each performing the exact same thing, but with different methods. 

### Version 1
This is the code for version 1: 
```
# v1. Test all divisors from 2 through n-1 (skip 1 and n)
def is_prime_v1(n):
    # Return true if n is a prime number, otherwise return false
    if n == 1:
        return False

    # Check for every i, if n is divisible
    for i in range(2, n):
        # If n is divisible by i -> not prime
        if n % i == 0:
            return False
        return True
```
In the is_prime_v1 function, there are basically two steps. 
1. If the number is 1, then return false (not a prime number)
2. Divide the number 2, 3, 4, ...., n - 1 and check if they are divisible by any of the numbers -> if yes, not prime, if no, prime 

This is what the function is telling the computer to do. Prime numbers are numbers that are only divisble by 1, and the number itself. 1 is not considered to be a prime number, thus the reason for the first if statement. If the number is not 1, then it divides the number with every integer in the range of 2 to the n - 1, with n being the number itself. If the number is divisible by any of the numbers in that range, this loses the possibilty of the number being prime, since it is divisible by other numbers, excluding 1 and the number itself. Thus the line `return False` inside `if n % i == 0:`. In the for loop, the range is set to `range(2, n)`. This means 2 to n-1; n would not be included in the range. For the last line, this is saying that else n is not divisible by any of the numbers in range, then it is prime number.

### Version 2
This is the code for version 2: 
```
# v2. Test all divisors from 2 through sqrt(n)
def is_prime_v2(n):
    if n == 1:
        # 1 is not prime
        return False

    max_divisor = math.floor(math.sqrt(n)) # Rounding down the sqrt
    for i in range(2, 1 + max_divisor):
        if n % i == 0:
            return False
        return True
```
This is_prime_v2 function does the same performance as the version 1 code, although there is a difference in the algorithm. 
In version 2, instead of dividing n with all the numbers from 2 to n-1, the program divides n from 2 to sqrt(n). 
```
18 = 1 x 18
   = 2 x 9
   = 3 x 6
   = 6 x 3
   = 9 x 2
   = 18 x 1
```
This is essentially what is being done in the first program. What we can see from here is that, the same calculation is being repeated. When exceeding the square root of the the number, the calculation would be the same as previous, just in different order. Therefore in the new program, instead of doing the calculation over and over, it reduces the amount of them, to make it more efficient. 
``` 
18 = 1 x 18 
   = 2 x 9
   = 3 x 6 
   = sqrt(18) x sqrt(18)
``` 
This would require less calculations, therefore is more time efficient. The line that saids `max_divisor = math.floor(math.sqrt(n))`, rounds down the number of the square root, so for example if the number was 1.3425, it would be 1. In the for loop command, `for i in range(2, 1 + max_divisor):`, it adds one to the max_divisor, or the rounded sqrt n, because when performing the loop, we want the sqrt to be accounted.


### Version 3 
This is the code for version 3:
```
# v3
# step 1) Test if n is even
# step 2) Test only odd divisors
def is_prime_v3(n):
    if n == 1:
        return False

    # IF it's even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_divisor, 2):
        if n % i == 0:
            return False
        return True
```
This code is the even more upgraded verion of the same program. Again, it has the same exact output, but it is only the matter of what algorithm it is using, how efficient it is. In this program, what is new is that, since we already know that 2 is a prime number, and that even number are not prime, since they are all divisible by 2, instead of dividing all the even numbers with the divisors from 2 to sqrt(n, we just created an if statement: 
```
if n == 2:
    return True 
if n > 2 and n % 2 == 0: 
    return False
```
This eliminates the process of doing unnecessary calculations. This program would automatically detect that every even number, except for 2, is not a prime number, therefore leaves the computer to only perform the calculations of the odd numbers, that potentially can be prime numbers. And the rest of the code is basically the same, although there is a slight difference in the for loop. 
```
for i in range(3, 1 + max_divsor, 2): 
```
As you can see in this line, there is a slight difference in the numbers of the range. First of all, the first divisor would be 3, because, the calculation is only for odd numbers, and since we already know that odd numbers are non-divisble by 2, we don't have to check that. `1 + max_divisor` is the same as version 2. This takes in account of the sqrt(n), and lastly, the interval of the range is set to 2. Basically what this means is that the odd number would only be divided by 3, 5, 7, 9, which makes sense, because if the interval was one, the computer would also have to calculate 4, 6, 8, and so on, which are all divisble by 2. And we know that odd numbers are never divisble by even numbers. This code is being as efficient as possible, eliminating the smallest unnecessary steps, to achieve the goal of finding prime numbers.


