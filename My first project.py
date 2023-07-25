import datetime
import time

import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


def escape():
    print("Thanks for using me, I hope we'll meet again!")
    print(colorama.Fore.LIGHTGREEN_EX + Style.BRIGHT + "The program will end in:")
    countdown()
    print("See You Again, Bye!!!")
    exit()


def calculator():
    operator = ["   +", "   -", "   *", "   /", "   % (Modulus)", "   ^ (Exponential)", "   ac (clear all)", "   x (exit)"]
    op_bullets = ["\u2022" + op for op in operator]
    initial = input("Enter the initial value or press x to exit: \n")
    if initial == "x":
        escape()
    elif type(initial) != "str" and type(initial) != "char":
        while True:
            for op in op_bullets:
                print(op)
            o = str(input("\n"))
            if o == "x":
                escape()
            elif o == "ac":
                calculator()
            n = float(input("Enter the Value\n"))
            match o:
                case "+":
                    initial = float(initial) + n
                    print(colorama.Fore.LIGHTGREEN_EX + "Your answer is " + str(initial))
                case "-":
                    initial = float(initial) - n
                    print(colorama.Fore.LIGHTGREEN_EX + "Your answer is " + str(initial))
                case "*":
                    initial = float(initial) * n
                    print(colorama.Fore.LIGHTGREEN_EX + "Your answer is " + str(initial))
                case "/":
                    if n == 0:
                        print(colorama.Fore.RED + "Your answer is " + "Denominator can not be Zero!!!\n continuing...")
                    else:
                        initial = float(initial) / n
                        print(colorama.Fore.LIGHTGREEN_EX + "Your answer is " + str(initial))
                case "%":
                    initial = float(initial) % n
                    print(colorama.Fore.LIGHTGREEN_EX + "Your answer is " + str(initial))
                case "^":
                    initial = float(initial) ** n
                    print(colorama.Fore.LIGHTGREEN_EX + "Your answer is " + str(initial))
                case _:
                    print(colorama.Fore.RED + "Your answer have " + "Error!!!\n Choose the operator correctly from the given options only.")
                    continue


def countdown():
    time.sleep(2)
    print(colorama.Fore.LIGHTGREEN_EX + Style.BRIGHT + "3\n")
    time.sleep(2)
    print(colorama.Fore.LIGHTGREEN_EX + Style.BRIGHT + "2\n")
    time.sleep(2)
    print(colorama.Fore.LIGHTGREEN_EX + Style.BRIGHT + "1\n")


t = str(datetime.datetime.now())
print(colorama.Fore.LIGHTYELLOW_EX + "Right now it's", colorama.Fore.YELLOW + Style.BRIGHT + t)
print("This program is use to evaluate binary arithmetic calculations!")
print(colorama.Fore.LIGHTGREEN_EX + Style.BRIGHT + "Program is initiating...")
countdown()
y = int(time.strftime("%H"))
if 4 < y < 12:
    print(colorama.Back.LIGHTCYAN_EX + Fore.BLACK + Style.NORMAL + "Good Morning Sir!!!, Running this python  code this early morning, you must be missing me so much. I'm more than happy to see you too. ;)")
elif 12 < y < 16:
    print(colorama.Back.LIGHTCYAN_EX + Fore.BLACK + Style.NORMAL + "Good Afternoon Sir!!!, It's really a great weather in the middle of this day and seeing you in this weather is apple to my eye")
elif 16 < y < 19:
    print(colorama.Back.LIGHTCYAN_EX + Fore.BLACK + Style.NORMAL + "Good Evening Sir!!!, Hope you are enjoying your day. I was getting board but waiting for you felt worth it.")
else:
    print(colorama.Back.LIGHTCYAN_EX + Fore.BLACK + Style.NORMAL + "It's the ending of the day Sir and you look exhausted  too, I know you wanna talk to me, but you should go to your bed. \n Good night Sir!")


def f_s():
    s = str(input("\nPress S if you want to continue using me, or press x to close the program\n"))
    if s == "s":
        print("Allow me to be in use for some time")

        def f_k():
            k = str(input("Press C to open calculator or x to exit\n"))
            if k == "c":
                print("Opening Calculator in:")
                countdown()
                calculator()
            elif k == "x":
                escape()
            else:
                print(colorama.Fore.RED + Style.BRIGHT + "You have entered the wrong command!!!")
                f_k()
        f_k()
    elif s == "x":
        escape()
    else:
        print(colorama.Fore.RED + Style.BRIGHT + "You have entered the wrong command!!!")
        f_s()


f_s()
