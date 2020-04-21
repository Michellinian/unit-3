Narrative programming with OOP practice. The following paragraph is a narration of a program developed by Sandi Metz (She is an awesome programmer in Ruby). Your task is to write the code that corresponds to that narration. 

In the application for a bicycle tour company, there is a class called Bicycle, with 3 instance attributes: size, chain, and tire size. The constructor also includes a call to the method post_initialize that takes the tire size and prints the circumference of the wheel. The instance attributes have default values as: tyre size=29 inches, chain=11 speed, and size= M. In this class there is another method called spares which prints the tyre size and the chain size. The class also has a class attribute called number of bicycles which is increased by one every time a new object of this class is created. 

In this application there is another class called Mountain Bike that inherits from the Bicycle class. It has two additional instance attributes: front fork and rear shock, which indicate the travel distance in millimeters of the front and back suspension of the mountain bike.  The default tyre size for a mountain bike is 27.5. The default front fork is 100 mm and rear shock is 80 mm. The class has a class attribute for the number of mountain bikes.

In the main application there is a list that stores the objects of bicycles and mountain bikes created.

```
import math

class Bicycle:
    numBike = 0

    def __init__(self, size="M", chain=11, tireSize=29):
        self.size = size
        self.chain = chain
        self.tireSize = tireSize
        self.post_intialize()
        self.spares()
        Bicycle.numBike += 1

    def post_intialize(self):
        circ = 2*math.pi*self.tireSize
        print(f"Circumference of the wheel: {circ}")

    def spares(self):
        print(f"Tire size: {self.tireSize}")
        print(f"Chain size: {self.chain}")

t100 = Bicycle("m", 10, 80)
t200 = Bicycle("l", 19, 30)
print(Bicycle.numBike)

class mountainBike(Bicycle):
    numMount = 0

    def __init__(self, size, chain, tireSize=27.5,frontfork=100, rearshock=80,):
        super().__init__(size, chain, tireSize)
        self.frontfork = frontfork
        self.rearshock = rearshock
        mountainBike.numMount += 1

m189 = mountainBike("m", 11)
m186 = mountainBike("m", 32)
print(mountainBike.numMount)

def mainApp():
    list = []
    totalNum = mountainBike.numMount + Bicycle.numBike
    for i in range(totalNum):
        list.append(Bicycle)
        list.append(mountainBike)
    print(list)
mainApp()
```

For this assignment I got it until the second task. I was able to make a class bicycle with all of the things that were asked, and they are all working without error, and so does the class mountainBike. One difficulty was finding how to manipulate class attributes. After learning that the syntax is `classname.classattribute`, it was easy to write the code for counting the objects. Although I am having a hard time creating the last bit of the task which is to store all the objects into a list. I need to figure out how to append in a list without having to assign each variable and say, `list.append(variable)`. Because when we create an object that object should automatically be appended in the list.
