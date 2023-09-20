import json
import os
class User: 
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        pass

class UserReository:
    def __init__(self):
        self.users = [] # all registered users
        self.isLoggedIn = False
        self.currentUser = {}

        #load users form json file
        self.loadUser()

    def loadUser(self):
        if os.path.exists("users.json"):
            with open("users.json","r") as file:
                users = json.load(file) # takes file -like objects
                for user in users:
                    user = json.loads(user) # takes string, returns dict
                    newUser = User(username= user["username"], password=user["password"], email=user["email"])
                    self.users.append(newUser)
            # print(self.users)

    def register(self,user: User):  # type annotiation
        self.users.append(user)
        self.saveToFile()
        print("User account is created. ")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user # choose the current user and assign it 
                print("logged in")
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("logged out. ")

    def identity(self):
        if self.isLoggedIn == True:
            print(f"username: {self.currentUser.username}")
        else :
            print("Did not logged in. ")

    def saveToFile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open ("users.json", "w") as file:
            json.dump(list, file)

repository = UserReository()

while True: 
    print('Menu'.center(50,'*'))
    choice = input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nYour choice: ')
    if choice == '5':
        break
    else:
        if choice =="1":
            username = input('username: ')
            password  = input('password: ')
            email = input('email: ')

            user = User(username=username, password=password, email=email)
            repository.register(user)

            print(repository.users)

        elif choice =="2":
            username = input('username: ')
            password  = input('password: ') 

            repository.login(username,password)
        elif choice =="3":
            repository.logout()
        elif choice =="4":
            repository.identity()
        else: 
            print("invalid input!!!")

