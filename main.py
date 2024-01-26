import base64
import hashlib
import os
import sys
from crypto import encrypt_message, decrypt_message
from store import delete_history, show_entry, store_entry
from en import strings

from utils import get_key, getDate

password_file = "password.cache"

app_state = dict(password=None, filename=None)


def hash_password(password):
    # Hash a password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


def validate_password(password):
    hashed_password = hash_password(password)

    with open(password_file, "r") as f:
        stored_password = f.read()

    # compare passwords
    if hashed_password == stored_password:
        app_state["password"] = password
        return True
    else:
        return False


def has_password():
    if os.path.isfile(password_file):
        return True
    else:
        return False


def create_password(password):
    # hash the password and store it in a file
    hashed_password = hash_password(password)
    with open(password_file, "w") as f:
        f.write(hashed_password)


def login():
    possible_tries = 3
    while possible_tries > 0:
        password = input("Enter password: ")
        if (validate_password(password)):
            if (app_state["filename"]):
                show_entry(app_state["filename"], app_state["password"])
            show_menu()
            break
        else:
            possible_tries -= 1
            print("❌ Password is incorrect. You have {} tries left".format(
                possible_tries))


def signup():
    password = input("Create new password: ")
    create_password(password)
    print("✅ Password created")


def new_entry():
    print("New entry, {} : ".format(getDate()))
    entry = input()
    encrypted_message = encrypt_message(entry, get_key(app_state["password"]))
    store_entry(encrypted_message)


def delete_option():
    delete_history()


def exit():
    print("🚪 Exiting...")
    sys.exit()


def show_menu():
    print("1️⃣ New Entry")
    print("2️⃣ Erase History")
    print("3️⃣ Exit")
    choice = input("Enter your choice: ")
    if (choice == "1"):
        new_entry()
    elif (choice == "2"):
        delete_option()
    elif (choice == "3"):
        exit()
    else:
        print("🔢 Invalid choice")

    show_menu()

def main():
    print(strings["welcome"])
    if len(sys.argv) == 2:
        app_state["filename"] = sys.argv[1]
        print(f"Login to see the file: {app_state['filename']}")

    if (has_password()):
        login()
    else:
        signup()


if __name__ == "__main__":
    main()
