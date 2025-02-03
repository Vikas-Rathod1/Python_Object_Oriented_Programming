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
                     5. Presss any other key to Exit""")
        
        if user_input == "1":
            pass
    

        elif user_input == "2":
            pass

        elif user_input == "3":
            pass

        elif user_input == "4":
            pass

        else: 
            exit()


obj = ChatBook()