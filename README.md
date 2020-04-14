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

## Registration

The preview for the login and sign up page are both inside the Appendix folder. 

For the sign up page, there are four input boxes for the user. The user has to enter ther email address, username, password, and same password for confirmation. In this sign up page these are the requirements:

1. Users are able to type in the line edits
2. WHen sign up button is pressed it should show if the information typed in are valid or not

For criteria number 2, to be more specific, when password typed in is all number or all letters, then the border of the text box should turn red, indicating that the information input by the user is invalid. Same goes for when the password for confirmation does not match the password user typed in the password text box. Also when there are text boxes that are not filled that text box should also turn red. 

When focusing on the requirements there were many requirements to cover, so I divided the work in to three. I created three different functions that perform the three actions for requirement number 2, and tested each of them if that works correctly. Then after checking that each program is working without malfunction, I decided to merge all the functions into one so that the code can be more efficient with less repitition of the same program. 

**Match Password**

This function checks if the two passwords typed in by the user are matching or not. If it matches then it should automatically go inside to the main page, otherwise it should the error by changing the dolor of the border of the box. 
Here is the code: 
```
    def matchPassword(self):
        password = self.lineEdit_4.text()
        confirmpass = self.lineEdit_2.text()

        if password != confirmpass:
            self.lineEdit_4.setStyleSheet("border: 2px solid red")
            self.lineEdit_2.setStyleSheet("border: 2px solid red")
            return
```
This code is located inside the signUpWindow class, since this is a method only used inside the sign up page. `self.lineEdit_4.text()` refers to the text input in the password box. The variables inside this function stores the user input. Down below in the if statement it is comparing the two inputs made by the users. `setStyleSheet()` is the syntax for using css to change the layout of the page. In this case I set the border color to be red only if the two passwords are not the same, so it indicated the invalid information to the user.

**If Empty**

This function focuses on checking if the user missed out on any information. If it detectd an empty box or boxes without information types in it would automatically indicate the user to type those in. Here is the code:
```
    def ifEmpty(self):
        username = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        confirmpass = self.lineEdit_2.text()
        email = self.lineEdit_1.text()

        if username == "":
            self.lineEdit_3.setStyleSheet("border: 2px solid red")
        else:
            self.lineEdit_3.setStyleSheet("border: 2px solid blue")
        if password == "":
            self.lineEdit_4.setStyleSheet("border: 2px solid red")
        else:
            self.lineEdit_4.setStyleSheet("border: 2px solid blue")
        if confirmpass == "":
            self.lineEdit_2.setStyleSheet("border: 2px solid red")
        else:
            self.lineEdit_2.setStyleSheet("border: 2px solid blue")
        if email == "":
            self.lineEdit_1.setStyleSheet("border: 2px solid red")
        else:
            self.lineEdit_1.setStyleSheet("border: 2px solid blue")
```
This is a code with simple if statements. These if statements detect whether the information contained in the box is null or not. It goes through every text boxes and show the result. 

**Invalid Password**

Finally for this function, it checks the validity of the password. If the password is only numbers or only letters it gives out error. Here is the code for this program:
```
    def invalidPass(self):
        password = self.lineEdit_4.text()

        if password.isdigit() or password.isalpha():
            self.lineEdit_4.setStyleSheet("border: 2px solid red;")
            return "invalid input"
        else:
            self.lineEdit_4.setStyleSheet("border: 2px solid blue;")
            return "valid input"
```
This is also a simple if statement. If the password is all digit, or if the password is all alpha, meaning letters, then the border of the text box would become red. If the passord is not, and is a mixture of both, then it would show a blue indicating that the password is valid.

### The entire program for sign up page 
```
class signupWindow(signupForm):
    def __init__(self, parent=None):
        super(signupWindow, self).__init__(parent)
        self.setupUi(self)

        self.lineEdit_1.setPlaceholderText("2020.uwc.isak@uwcisak.jp")
        self.lineEdit_3.setPlaceholderText("uwc isak")
        self.lineEdit_4.setPlaceholderText("mixture of letters and numbers")
        self.lineEdit_2.setPlaceholderText("Enter the same password")
        # pushButton_2 = loginButton
        # If the user already has an account go back to the login page
        self.pushButton_2.clicked.connect(self.openlogin)
        self.pushButton.clicked.connect(self.regCheck)

    def openlogin(self):
        login = loginWindow(self)
        login.show()

    def openMain(self):
        main = mainWindow(self)
        main.show()

    def regCheck(self):
        username = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        confirmpass = self.lineEdit_2.text()
        email = self.lineEdit_1.text()

        # Create list variable
        passList = []

        if username == "":
            self.lineEdit_3.setStyleSheet("border: 2px solid red")
            passList.append("invalid")
        else:
            self.lineEdit_3.setStyleSheet("border: 2px solid blue")
            passList.append("pass")
        if password == "" or password.isalpha() or password.isdigit():
            self.lineEdit_4.setStyleSheet("border: 2px solid red")
            passList.append("invalid")
        else:
            self.lineEdit_4.setStyleSheet("border: 2px solid blue")
            passList.append("pass")
        if confirmpass == "" or confirmpass.isdigit() or confirmpass.isalpha():
            self.lineEdit_2.setStyleSheet("border: 2px solid red")
        else:
            if confirmpass == password:
                self.lineEdit_2.setStyleSheet("border: 2px solid blue")
                passList.append("pass")
        if email == "":
            self.lineEdit_1.setStyleSheet("border: 2px solid red")
        else:
            self.lineEdit_1.setStyleSheet("border: 2px solid blue")
            passList.append("pass")
```

One issue while I was developing this program is that, I couldn't change the name of each text boxes and buttons. I said `setObjectName` and trid to change the names of these, so then it would be much easier. Although I couldn't manage to do this.

In this code, first I have method called "openlogin", which gets called only when the login button in the page is pressed by the user. This button is for the people who already have an account and don't need to create a new one. This operation is controlled by the line `self.pushButton_2.clicked.connect(self.openlogin)`.

The the second method is called "openMain". This function should only be called when the sign up button is pressed, under the circumstance that all the required information by the user is typed correctly, without any errors. This "checking the information" is done by the "regCheck" method. 

In the regCheck method, it contains all the three functions, "match pwd", "if emtpy", and "invalid pwd". It does the exact same thing, the difference is that they're all in one. Which is why there are many conditions inside the method. 

Although one problem was that I didn't know how to write a program so that the if all the information are correctly typed in then it would automatically go to the main page. So I had to modify some of the code in order to get the functionalit that I was looking for and this is the final code of the sign up page.

```
    def openlogin(self):
        login = loginWindow(self)
        login.show()

    def openMain(self):
        main = mainWindow(self)
        email = self.lineEdit_1.text()
        username = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        confirmpass = self.lineEdit_2.text()
        if self.checkMail(email) is True and self.checkUsername(username) is True and self.checkPwd(password) is True and self.conPass(password, confirmpass) is True:
            main.show()

    def checkPwd(self, password):

        if password == "" or password.isalpha() or password.isdigit():
            self.lineEdit_4.setStyleSheet("border: 2px solid red")
        else:
            self.lineEdit_4.setStyleSheet("border: 2px solid blue")
            return True

    def conPass(self, password, confirmpass):
        if confirmpass == "" or confirmpass.isdigit() or confirmpass.isalpha():
            self.lineEdit_2.setStyleSheet("border: 2px solid red")
        else:
            if confirmpass == password:
                self.lineEdit_2.setStyleSheet("border: 2px solid blue")
                return True

    def checkUsername(self, username):
        if username == "":
            self.lineEdit_3.setStyleSheet("border: 2px solid red")
        else:
            self.lineEdit_3.setStyleSheet("border: 2px solid blue")
            return True

    def checkMail(self, email):
        if email == "":
            self.lineEdit_1.setStyleSheet("border: 2px solid red")
        else:
            self.lineEdit_1.setStyleSheet("border: 2px solid blue")
            return True
```
In this program what is different is that I actually divided the functions back into small bits. What I wanted to do was that I wanted to check if all the functions return True or not, and if does then it should open the main page. This is why I seperated all the functions so that it can either return true or nothing for each one. I feel like there is an easier way, for example I use the paramter password in two differnt functions, and I don't know but I feel like there might be a way of not having to repeat the same parameter. Although this is the best I could do. The program works well, and the main page only opens when all of the functions are checked and if all of them return true.

## Login in 

In the login page, what the user needs to be able to do is to type in their username and password, and if they entered the correct information, then they should be able to go inside the main page. The username and the password should come from the information they entered in the sign up page. Only if the typed in information in the login page, matches with the information that the user typed in for registration previously, then they should be able to access their inventory. 



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


## Testing sign up page



