class ChatBook:
    def __init__(self) -> None:
        #print("----",self)
        self.__name = "default user"
        self.username = ""
        self.password = ""
        self.loggedin = False
        # self.menu()


    def get_name(self):

        return self.__name
    
    def set_name(self, value):
        #self.__name = input("Enter your name: ")
        self.__name = value

    def menu(self):
        user_input = input("""Welcome to the Chatbook.How would you you like to proceed?
                     1. Press 1 to signup
                     2. Press 2 to signin
                     3. Press 3 to write a post
                     4. Press 4 to messsage a friend
                     5. Presss any other key to Exit
                
                           
                    ->""")
        
        if user_input == "1":
            self.signup()
    

        elif user_input == "2":
            self.signin()

        elif user_input == "3":
            self.my_post()

        elif user_input == "4":
            self.send_message()

        else: 
            exit()

    def signup(self):
        email = input("Enter you mail here -->")
        passwrd = input("Enter your Password here -->")

        self.username = email
        self.password  = passwrd
        print("You have signup successfully !!")
        print("Thank you so much !!\n\n")
        self.menu()

    def signin(self):
        if self.username=="" and self.password =="":
            print("Please signup first by clicking 1 in the menu")
        else:
            usernam = input("Enter your email/username here -->")
            passwrd = input("Enter your passwrod here -->")

            if self.username==usernam and self.password==passwrd:
                print("You have signed in successfully !!")
                self.loggedin = True

            else:
                print("Please input correct Credentials...")
            print("\n")
            self.menu()



    def my_post(self):
        if self.loggedin == True:
            print("You are logged in !!")
            text = input("Enter you message here......->")

            print(f"You can see your posted here !! {text}")
        else:
            print("Please signin first !!")
            print("\n")

            self.menu()
    def send_message(self):
        if self.loggedin == True:
            print("You are logged in !!")
            text = input("Enter you message here......->")
            frnd = input("Whome do you want to send the message -->")
            print(f"Your message has been send to {frnd}")
            self.menu()
        else:
            print("Please signin first !!")
            print("\n")
            self.menu()
obj = ChatBook()
# obj.name = "VikasRathod"
# print(obj.name)
# print("....",id(obj))
# #obj.signup()
# obj1 = ChatBook()
# print("..+..",id(obj1))