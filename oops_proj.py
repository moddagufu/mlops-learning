class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.logged_in=False
        self.menu()

    def menu(self):
        user_input=input("""Welcome to chatbook how would you like to proceed?"
                         1.press 1 to signup
                         2.press 2 to login
                         3.press 3 to write a post
                         4.press 4 to message a friend
                         5.press 5 to logout""")
        
        if user_input=='1':
            self.signup()
        elif user_input=='2':
            self.login()
        elif user_input=='3':
            self.write_post()
        elif user_input=='4':
            self.message_friend()
        elif user_input=='5':
            self.logout()
        else:
            exit()
    
    def signup(self):
        email=input("Enter your email")
        pwd=input("Enter your password")
        self.username=email
        self.password=pwd
        print("Signup successful")
        print("\n")
        self.menu()

    def login(self):
        if self.username=='' and self.password=='':
            print("No user found, please signup first")
        else:
            username=input("Enter your email")
            pwd=input("Enter your password")
            if self.username==username and self.password==pwd:
                self.logged_in=True
                print("Login successful")
            else:
                print("Invalid credentials")
        print("\n")
        self.menu()

    def write_post(self):
        if self.logged_in:
            post=input("Write your post here:")
            print("Post published:", post)
        else:
            print("Please login to write a post")
        print("\n")
        self.menu()

    def message_friend(self):
        if self.logged_in:
            friend=input("Enter your friend's name:")
            message=input("Enter your message:")
            print(f"Message sent to {friend}: {message}")
        else:
            print("Please login to message a friend")
        print("\n")
        self.menu()

    def logout(self):
        if self.logged_in:
            self.logged_in=False
            print("Logged out successfully")
        else:
            print("You are not logged in")
        print("\n")
        self.menu()

user1= chatbook()
        
       