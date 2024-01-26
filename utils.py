import base64
import datetime


def getDate():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_key(password):
    key = password.encode()
    encoded_key = base64.urlsafe_b64encode(key.ljust(32, b'\0')[:32])

    return encoded_key


if __name__ == "__main__":
    print(getDate())
