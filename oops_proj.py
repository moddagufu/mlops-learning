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

obj= chatbook()
        
       