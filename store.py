from crypto import decrypt_message
from utils import get_key, getDate
import os


entries_dir = "entries"


def create_entries_dir():
    if not os.path.isdir(entries_dir):
        os.mkdir(entries_dir)


def store_entry(entry):
    create_entries_dir()
    filename = "entries/{}.txt".format(getDate())
    with open(filename, "ba") as f:
        f.write(entry)
    print("Entry stored successfully")


def show_entry(filename, password):
    with open(filename, "rb") as f:
        encrypted_message = f.read()
    decrypted_message = decrypt_message(encrypted_message, get_key(password))
    print("============= Entry: {} ===============".format(filename))
    print(decrypted_message)
    print("============ End of File ==============".format(filename))


def delete_history():
    for filename in os.listdir(entries_dir):
        os.remove(os.path.join(entries_dir, filename))
    print("History deleted successfully")
