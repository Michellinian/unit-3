② Narrative programming with OOP practice. The following paragraph is a narration of a program developed by Sandi Metz (She is an awesome programmer in Ruby). Your task is to write the code that corresponds to that narration. 


In the application for a bicycle tour company, there is a class called Bicycle, with 3 instance attributes: size, chain, and tire size. The constructor also includes a call to the method post_initialize that takes the tire size and prints the circumference of the wheel. The instance attributes have default values as: tyre size=29 inches, chain=11 speed, and size= M. In this class there is another method called spares which prints the tyre size and the chain size. The class also has a class attribute called number of bicycles which is increased by one every time a new object of this class is created. 


In this application there is another class called Mountain Bike that inherits from the Bicycle class. It has two additional instance attributes: front fork and rear shock, which indicate the travel distance in millimeters of the front and back suspension of the mountain bike.  The default tyre size for a mountain bike is 27.5. The default front fork is 100 mm and rear shock is 80 mm. The class has a class attribute for the number of mountain bikes.


In the main application there is a list that stores the objects of bicycles and mountain bikes created.
