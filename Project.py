class ChatBook:
    def __init__(self) -> None:
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()


    def menu(self):
        user_input = input("""Welcome to the Chatbook.How would you you like to proceed?
                     1. Press 1 to signup
                     2. Press 2 to signin
                     3. Press 3 to write a post
                     4. Press 4 to messsage a friend
                     5. Presss any other key to Exit
                \nThis is the place where you can press \n""")
        
        if user_input == "1":
            self.signup()
    

        elif user_input == "2":
            pass

        elif user_input == "3":
            pass

        elif user_input == "4":
            pass

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



    


obj = ChatBook()

#obj.signup()