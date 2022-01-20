import os
import time
from tabulate import tabulate

class MyTextFormat:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def cprint(cstr):
    print(cstr.center(os.get_terminal_size().columns))
def cclear():
    os.system("clear")

def welcome():
    cclear()
    cprint(MyTextFormat.YELLOW + "Welcome to GT-Toolbox" + MyTextFormat.END)
    time.sleep(1)
    while True:
        cclear()
        print(tabulate(options, headers = 'firstrow', tablefmt = 'grid'))
        key = input("Press a key to continue...\n")
        if key == '0':
            cprint(MyTextFormat.YELLOW + "Thanks for using my toolbox!" + MyTextFormat.END)
            time.sleep(1)
            cclear()
            break

options = [['Function', 'Key'], ['Lemke-Howson algorithm', '1'], ['Exit', '0']]

welcome()