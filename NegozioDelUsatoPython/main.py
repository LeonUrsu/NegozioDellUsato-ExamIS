import datetime
import json
import bcrypt
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("ciao")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Test:
    def __init__(self, var,var2):
        self.var = var
        self.var2 = var2


print('-------------------------')
test1 = Test(1,4)
test2 = Test(2,5)





"""
date_format = '%d/%m/%Y, %H/%M/%S'
today = datetime.today()
tomorrow = datetime.today() + timedelta(minutes=1)
if tomorrow >= today:
    print('ciao')
print(today, tomorrow)
"""



"""
def welcome():
    print("Benvenuto alla tua dashboard")


def gainAccess(Username=None, Password=None):
    Username = input("Inserisci il tuo username:")
    Password = input("Inserisci la tua Password:")

    if not len(Username or Password) < 1:
        if True:
            db = open("Database/Clienti/Clienti.txt", "r")
            d = []
            f = []
            for i in db:
                a, b = i.split(",")
                b = b.strip()
                c = a, b
                d.append(a)
                f.append(b)
                data = dict(zip(d, f))
            try:
                if Username in data:
                    hashed = data[Username].strip('b')
                    hashed = hashed.replace("'", "")
                    hashed = hashed.encode('utf-8')

                    try:
                        if bcrypt.checkpw(Password.encode(), hashed):

                            print("Login success!")
                            print("Hi", Username)
                            welcome()
                        else:
                            print("Password errata!")

                    except:
                        print("Password o Username non corretti")
                else:
                    print("Username non esiste")
            except:
                print("Password o Username inesistenti")
        else:
            print("Errore nel login del sistema")

    else:
        print("Perfavore prova un altro tentativo")
        gainAccess()

    # b = b.strip()


# accessDb()

def register(Username=None, Password1=None, Password2=None):
    Username = input("Inserisc username:")
    Password1 = input("Create password:")
    Password2 = input("Confirm Password:")
    db = open("Database/Clienti/Clienti.txt", "r")
    d = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        c = a, b
        d.append(a)
    if not len(Password1) <= 8:
        db = open("Database/Clienti/Clienti.txt", "r")
        if not Username == None:
            if len(Username) < 1:
                print("Please provide a username")
                register()
            elif Username in d:
                print("Username exists")
                register()
            else:
                if Password1 == Password2:
                    Password1 = Password1.encode('utf-8')
                    Password1 = bcrypt.hashpw(Password1, bcrypt.gensalt())

                    db = open("Database/Clienti/Clienti.txt", "a")
                    db.write(Username + ", " + str(Password1) + "\n")
                    print("User created successfully!")
                    print("Please login to proceed:")


                # print(texts)
                else:
                    print("Passwords do not match")
                    register()
    else:
        print("Password too short")


def home(option=None):
    print("Welcome, please select an option")
    option = input("Login | Signup:")
    if option == "Login":
        gainAccess()
    elif option == "Signup":
        register()
    else:
        print("Please enter a valid parameter, this is case-sensitive")


#register(Username, Password1, Password2)
#gainAccess(Username, Password1)
home()
"""