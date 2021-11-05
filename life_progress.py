# STREAK TRACKER

import os
import datetime
from typing import Counter


FILE = 'birthdate.txt'
LIFE_EXPECTANCY = 83.64

DAYS_EXPECTANCY = round(LIFE_EXPECTANCY * 365)

today = datetime.date.today()


SQUARE = '▩'
FILLED = '●'
UNFILLED = '○'
CGREEN  = '\33[32m'
CRED    = '\033[91m'
CEND    = '\033[0m'


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def get_user():
    if os.environ.get('USER'):
        return os.environ.get('USER')
    elif os.environ.get('USERNAME'):
        return os.environ.get('USERNAME')
    else:
        return "USER"


def get_days_since_birth():
    with open(FILE, 'r') as file:
        birthdate_txt = file.readlines()
    days_since = datetime.datetime.today() - datetime.datetime.strptime(birthdate_txt[0], "%d-%m-%Y")
    return days_since.days


def print_squares(days_since_birth):
    days_left = DAYS_EXPECTANCY - days_since_birth
    count = 0
    for x in range(days_since_birth):
        if count % 7 == 0 and count != 0:
            print(" ", end='')
        print(CRED + FILLED + CEND, end='')
        count+=1
    for x in range(days_left):
        if count % 7 == 0:
            print(" ", end='')
        print(CGREEN + UNFILLED + CEND, end='')
        count+=1


def get_as_percentage(days_since_birth):
    return round((days_since_birth / DAYS_EXPECTANCY) * 100, 2)


def print_progress_bar(percentage):
    print('{', end='')
    for x in range(round(percentage)):
        print(CRED + SQUARE + CEND, end='')
    for x in range(100 - round(percentage)):
        print(CGREEN + SQUARE + CEND, end='')
    print('} ' + str(percentage) + '%\n')


def print_days_left(days_since_birth):
    days_left = DAYS_EXPECTANCY - days_since_birth
    print("You (probably) have " + str(days_left) + " days to live.\n\n")


def print_heading():
    print("""
    __    _ ____        ____                                      
   / /   (_) __/__     / __ \_________  ____ _________  __________ 
  / /   / / /_/ _ \   / /_/ / ___/ __ \/ __ `/ ___/ _ \/ ___/ ___/ 
 / /___/ / __/  __/  / ____/ /  / /_/ / /_/ / /  /  __(__  |__  ) 
/_____/_/_/  \___/  /_/   /_/   \____/\__, /_/   \___/____/____/  
                                     /____/                       
                                                                \n\n""")


# MAIN
clearConsole()
print_heading()
days_since_birth = get_days_since_birth()
percentage = get_as_percentage(days_since_birth)
print_progress_bar(percentage)
print_days_left(days_since_birth)
print_squares(days_since_birth)
