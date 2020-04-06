# program that accepts a string and calculate the number of digits and letters

usrin = input()
dig = sum(i.isdigit() for i in usrin)
let = sum(i.isalpha() for i in usrin)
print(f"Letters {let}")
print(f"Digitd {dig}")



