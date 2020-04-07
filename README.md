# Creating inventory 
Repo for unit 3

1. [Planning](#Planning)
2. [Design](#Design)
3. [Development](#Development)
4. [Evalutaion](#Evaluation)

Planning
====

### Defining the problem 
This is the email I received from my client: 

"Summer holidays start in a few months and I am starting to think of the packing process since I am going back home. I have been really worried I end up forgetting something important or that the number of things I have will not fit my bag and I may need to buy new luggage. For this reason, I need an inventory that will allow me to record the things that I have at the moment until the time when I start packing. This inventory needs to be divided into categories of type of items and its subtypes and must have a space for description, for example, the category clothes must have the subcategory of blouses and space where I can make a short description, eg: white with blue flowers. The things I have may vary a lot so I must be able to add any new category or subcategory to the system when I feel like the existing ones don’t categorize the item I need to add to the inventory."

To paraphrase this, my client, Lauricenia will be going back home by plane for this summer break, and she is having trouble keeping track of all the things she has to pack. At the moment she doesn't know how much belongings she has to bring home, and so she cannot decide if she should buy a new suitcase or not. She has the rest of the school year to figure this out, although she wants to make sure in advance of what and how much of things she has at the moment, to get an idea of what she can bring back home. 


### Solution proposed 
The solution is to create an inventory of packing list for my client so that she can keep track on her belongings. This inventory would be devided into categories, such as clothes, books, toiletries, etc. so that it is easier for her to spot ehat things she have in her room at the moment. It would also have subcategories, so for example, under clothes, there might be t-shirts, jackets, pants, etc. so that my client can have a better idea of her belongings. Since it is summer break and it is the longest break of the year, she wants to be precise about what she brings back home, to make sure that she has absolutely evrerything she needs throughout her entire summer. Also the inventory should record the amount of each belonging she has, as well as the total number of belongings per category and the total. Furthermore, weights of each category should be recorded, since she is getting on a plane for her transportation, and there is a limited number of weight per passenger. She needs to make sure that her luggage is not over the limit or else she would have to pay additional fee. Also by making the inventory editable, she can be able to add new categories, name the subcategories differently, update the weight of the belongings as well as the number, and so on. Finally to secure her inventory list, a secure login system will be required so that she is the only one who can check the inventory list. 

### Success Criteria
1. seperating her belongings into different categories
2. category of the belonging is also seperated into different subcategories 
3. offers spaces for description 
4. shows the total number of objects 
5. shows the number of objects per category
6. shows the weight of objects per category 
7. secure login system is created 
8. storation of data while not using the app

### Justification of tool 
This program uses python as a programming language, and the tool used is PyCharm, an IDE specificated for python. IDE makes the development of the program easier than online platform, since it allows us to create multiple folders and files, which makes it easier to keep track of programs, especially when creating less simple programs. Python would be a good programming language when creating programs or softwares, since python has very kind syntaxes, as well as easier way of doing certain algorithm that cannot be done in other programming languages. It is developer-friendly, and therefore the usage of python and PyCharm as the platform for the dvelopment of this particular software.


Design
====

### Sketch of the app 
![Appsketch](Appendix/appsketch.jpg)

This is the first sketch of the app that I will be developing for my client.

The main window is the table of belongings that are seperated in different categories. These categories are each seperated in different subcateogries, and these columns are set to be buttons so that these can be selected and jump to another page about the information of the selected categories, which is what the subwindow is. Also on the main page there are weights of different categories shown. In the subwindow, there is another table, and here it shows the name of the object as well as its description. At the bottom it shows the total number of things in the subcateogory, and the weight of the objects. Furthermore there is an edit button, where it allows the user to edit the name of the categories, subcategories as well as the description of objects, the name of the objects and the number of weight. 

In the login window there are boxes that requires the user to type in their password and their username, since the client wanted the inventory to be confidential to other people. Below those, there are two buttons one is login and the other is sign up. When the user already have an account and typed in their login information correctly, then they will be able to jump to the main window. When they don't have an account they would need to sign up and create an account first. The signup form int eh sketch is almost like all the other sign up page. By setting the username, password, and email address the user will be able to login and look for their own inventory. 

### Updates sketch of the app

Development
====

### Registration

First of all this is what the login/signup pages look like.
![loginpage](Appendix/login.png)
![signuppage](Appendix/signup.png)

For the sign up page, there are four input boxes for the user. The user has to enter ther email address, username, password, and same password for confirmation. In this sign up page these are the requirements:
1. Users are able to type in the line edits
2. WHen sign up button is pressed it should show if the information typed in are valid or not
For criteria number 2, to be more specific, when password typed in is all number or all letters, then the border of the text box should turn red, indicating that the information input by the user is invalid. Same goes for when the password for confirmation does not match the password user typed in the password text box. Also when there are text boxes that are not filled that text box should also turn red. 



Evaluation 
=== 

All the videos for proof are in the folder testAppendix.

## Testing the buttons 

This test is to evaluate the functionality of the buttons. It tests whether the button redirects the system to the right page, and whether it should perform the correct function. 

### Login Page
**Login Button**

This button should:
1. Check if the username is correct 
2. if the password is correct 
3. If both information are correct it should go in to the main page (their inventory)

**Signup Button**

This button should take the user to sign up form. 

### Signup Page
**Signup Button**

This button should:
1. Check if every detail are valid -> if not the boxes that contains invalid information should turn red
2. Go back to the login button 

**Login Button**

This button should go back to the login page.


### Testing sign up system 

