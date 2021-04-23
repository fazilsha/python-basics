class LoginSystem():
    userdb={"fazil":"fazil123","alex":"alex34"}
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def auth(self):
        if self.username in  self.userdb:
            if self.password == self.userdb[self.username]:
                print("Login succeeded!")
            else:
                print("incorrect password")
        else:
            print("User not found!!!")

user=input("Enter your  username: ")
pwd =input("Enter your password: ")
l = LoginSystem(user,pwd)
l.auth()
