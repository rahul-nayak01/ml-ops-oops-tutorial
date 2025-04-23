
class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu()
        

    def menu(self):
        user_input=input("""Welcome to chatbook , how would u like to proceed?
                                1. Press 1 to signup
                                2. Press 2 to signin
                                3. Press 3 to Write a post
                                4. Press 4 to messeage a friend
                                5. Press any other key to exit
                         \n""")
        if user_input =="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.post()
        elif user_input=="4":
            self.messeage()
        else:
            exit()


    def signup(self):
        email=input("Enter Ur EMail Here")
        pass1=input("Setup ur password here")
        self.username=email
        self.password=pass1
        print("Signup is Done Successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=="" and self.password=="":
            print("please signup first by pressing 1 in main menu ")
        else:
            uname=input("Enter ur email")
            pas=input("ENter ur password")
            if self.username==uname and self.password==pas:
                print("Signin is don sucessfully")
                self.loggedin=True
            else:
                print("Please i/p correcr details")
        print("\n")
        self.menu()

    def post(self):
        if self.loggedin==True:
            txt=input("Enter ur post")
            print(f"Following content {txt} is posted")
        else:
            print("you need to signin first")
        print("\n")
        self.menu()
    
    def messeage(self):
        if self.loggedin==True:
            msg=input("Enter ur message")
            friend=input("ENter friends name")
            print(f"Your message  {msg} is sent to {friend}")
        else:
            print("you need to signin first")
        print("\n")
        self.menu()

user1=chatbook()
