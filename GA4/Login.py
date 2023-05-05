# create a simple login and signup using file storage in a file named "logins.txt"

import os
import sys
import getpass

def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    if os.path.isfile("logins.txt"):
        with open("logins.txt", "r") as f:
            for line in f:
                if username in line:
                    if password in line:
                        print ("Login successful")
                        return
                    else:
                        print ("Wrong password")
                        return
            print ("Wrong username")
            return
    else:
        print ("No logins.txt file found")
        return
    
def signup():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    if os.path.isfile("logins.txt"):
        with open("logins.txt", "r") as f:
            for line in f:
                if username in line:
                    print ("Username already exists")
                    return
        with open("logins.txt", "a") as f:
            f.write(username + ":" + password)
            print ("Signup successful")
            return
    else:
        with open("logins.txt", "w") as f:
            f.write(username + ":" + password)
            print ("Signup successful")
            return
        
def main():
    while True:
        choice = input("1. Login, 2. Signup, 3. Exit: ")
        if choice == "1":
            login()
        elif choice == "2":
            signup()
        elif choice == "3":
            break
        else:
            print ("Invalid choice")
            continue

if __name__ == "__main__":
    main()
