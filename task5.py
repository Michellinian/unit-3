# Write a Python program to calculate a dog's age in dog's years. Go to the editor
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

class Dogs:
    def __init__(self, age):
        self.age = age
        self.ageCalculation()

    def ageCalculation(self):
        dogAge = 2*10.5+(self.age-2)*4
        print(dogAge)


