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
In version 2, instead of dividing n with the 




