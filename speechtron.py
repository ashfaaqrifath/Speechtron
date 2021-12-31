import pyttsx3
import colorama
from colorama import Fore, Back

colorama.init(autoreset=True)

speak1 = " Speechtron basic text narrator. Read file or enter text for narration. "
print(Fore.BLACK + Back.BLUE + speak1)
print("Copyright (c) 2022 Ashfaaq Rifath")
engine = pyttsx3.init()
engine.say(speak1)
engine.runAndWait()

usr_option = input(Fore.CYAN + "Read file or enter text (r/t)? ")

if usr_option.lower() == "t":
    engine = pyttsx3.init()
    engine.say("enter your text for narration")
    engine.runAndWait()

    user_input = input(Fore.YELLOW + "Enter your text for narration: ")
    engine = pyttsx3.init()
    engine.say(user_input)
    engine.runAndWait()

    speak3 = "Narration completed"
    print(Fore.GREEN + speak3)
    engine = pyttsx3.init()
    engine.say(speak3)
    engine.runAndWait()

elif usr_option.lower() == "r":
    engine = pyttsx3.init()
    engine.say("Current path or absolute path")
    engine.runAndWait()

    usr_file_path = input(Fore.CYAN + "Current path or absolute path (c/a)? ")

    if usr_file_path.lower() == "c":
        engine = pyttsx3.init()
        engine.say("Enter file name")
        engine.runAndWait()

        c_path = input(Fore.YELLOW + "Enter file name: ")
        with open(c_path, 'rb') as file:
            reading_file1 = file.read()
        engine = pyttsx3.init()
        engine.say(reading_file1)
        engine.runAndWait()

        speak4 = "Narration completed"
        print(Fore.GREEN + speak4)
        engine = pyttsx3.init()
        engine.say(speak4)
        engine.runAndWait()

    elif usr_file_path.lower() == "a":
        engine = pyttsx3.init()
        engine.say("Enter file path")
        engine.runAndWait()

        a_path = input(Fore.YELLOW + "Enter file path: ")
        with open(a_path, 'rb') as file:
            reading_file2 = file.read()
        engine = pyttsx3.init()
        engine.say(reading_file2)
        engine.runAndWait()

        speak5 = "Narration completed"
        print(Fore.GREEN + speak5)
        engine = pyttsx3.init()
        engine.say(speak5)
        engine.runAndWait()