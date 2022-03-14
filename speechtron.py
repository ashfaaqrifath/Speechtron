import pyttsx3
from pathlib import Path
import string
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

def Speechtron(speak):
    engine = pyttsx3.init()
    engine.say(speak)
    engine.runAndWait()

def showMessage(message):
    if message == "2":
        print(Fore.BLACK + Back.RED + " INVALID OPTION ")
        Speechtron("INVALID OPTION")
    elif message == "3":
        print(Fore.BLACK + Back.RED + " FILE NOT FOUND ")
        Speechtron(" FILE NOT FOUND ")
    elif message == "4":
        print("File name already exists")
        Speechtron("File name already exists")

def narrateComplt(count):
    word_count = sum([i.strip(string.punctuation).isalpha() for i in count.split()])
    print(Fore.GREEN + "Narration completed. " + "(" + str(word_count) + " words)")
    Speechtron("Narration completed. " + str(word_count) + "words")


print(Fore.BLACK + Back.BLUE + " Speechtron text to speech. Enter file or text for narration. ")
Speechtron("Speechtron text to speech. Enter file or text for narration.")

usr_option = input(Fore.CYAN + "Read file or enter text (r/t): ")

var1 = ['r', 'R', 't', 'T']
while usr_option not in var1:
    showMessage(message="2")
    usr_option = input(Fore.CYAN + "Read file or enter text (r/t): ")

if usr_option.lower() == "t":
    Speechtron("Enter your text for narration")
    user_input = input(Fore.YELLOW + "Enter your text for narration: ")
    word_count = sum([i.strip(string.punctuation).isalpha() for i in user_input.split()])
    saving = "narrating user input. " + user_input + ". narration completed. " + str(word_count) + "words."
    Speechtron(user_input)

    narrateComplt(count=user_input)
    Speechtron("Do you want to save audio file")
    save_ask = input("Do you want to save audio file (y/n): ")

    var2 = ['y', 'Y', 'n', 'N']
    while save_ask not in var2:
        showMessage(message="2")
        save_ask = input("Do you want to save audio file (y/n): ")

    if save_ask.lower() == "y":
        Speechtron("Name your file")
        naming_file = input("Name your file: ")

        path_to_file = naming_file + ".mp3"
        path = Path(path_to_file)
        if path.is_file():
            showMessage(message="4")

        engine = pyttsx3.init()
        engine.save_to_file(saving, naming_file + '.mp3')
        engine.runAndWait()
        print(f"{naming_file}.mp3 audio file saved")
        Speechtron(f"{naming_file}.mp3 audio file saved")

elif usr_option.lower() == "r":
    Speechtron("Current path or absolute path")
    usr_file_path = input(Fore.CYAN + "Current path or absolute path (c/a): ")

    var3 = ['c', 'C', 'a', 'A']
    while usr_file_path not in var3:
        showMessage(message="2")
        usr_file_path = input(Fore.CYAN + "Current path or absolute path (c/a): ")

    if usr_file_path.lower() == "c":
        Speechtron("Enter file name")
        c_path = input(Fore.YELLOW + "Enter file name: ")

        path_to_file = c_path
        path = Path(path_to_file)

        if path.is_file():
            print(f"Narrating file: {c_path}")
            Speechtron(f"Narrating file: {c_path}")
            with open(c_path, 'rb') as file:
                reading_file1 = file.read()
                #converting bytes to string, because some text might be in bytes when copy paste.
                narrate = str(reading_file1, 'UTF-8')
                print(narrate)
                word_count = sum([i.strip(string.punctuation).isalpha() for i in narrate.split()])
                savefile = f"narrating file: {c_path}. " + narrate + " Narration completed. " + str(word_count) + "words."
            Speechtron(narrate)

            narrateComplt(count=narrate)
            Speechtron("Do you want to save audio file")
            save_ask = input("Do you want to save audio file (y/n): ")

            if save_ask.lower() == "y":
                Speechtron("Name your file")
                naming_file = input("Name your file: ")

                path_to_file = naming_file + ".mp3"
                path = Path(path_to_file)
                if path.is_file():
                    showMessage(message="4")

                engine = pyttsx3.init()
                engine.save_to_file(savefile, naming_file + ".mp3")
                engine.runAndWait()
                print(f"{naming_file}.mp3 audio file saved")
                Speechtron(f"{naming_file}.mp3 audio file saved")
        else:
            showMessage(message="3")

    elif usr_file_path.lower() == "a":
        Speechtron("Enter file path")
        a_path = input(Fore.YELLOW + "Enter file path: ")

        path_to_file = a_path
        path = Path(path_to_file)

        if path.is_file():

            with open(a_path, 'rb') as file:
                print("Narrating absolute path file.")
                Speechtron("Narrating absolute path file.")

                reading_file2 = file.read()
                # converting bytes to string, because some text might be in bytes when copy paste.
                narrate = str(reading_file2, 'UTF-8')
                print(narrate)
                word_count = sum([i.strip(string.punctuation).isalpha() for i in narrate.split()])
                savefile = f"narrating file: {a_path}. " + narrate + " Narration completed." + str(word_count) + "words."
            Speechtron(narrate)

            narrateComplt(count=narrate)
            Speechtron("Do you want to save audio file")
            save_ask = input("Do you want to save audio file (y/n): ")

            if save_ask.lower() == "y":
                Speechtron("Name your file")
                naming_file = input("Name your file: ")

                path_to_file = naming_file + ".mp3"
                path = Path(path_to_file)
                if path.is_file():
                    showMessage(message="4")

                engine = pyttsx3.init()
                engine.save_to_file(savefile, naming_file + ".mp3")
                engine.runAndWait()
                print(f"{naming_file}.mp3 audio file saved")
                Speechtron(f"{naming_file}.mp3 audio file saved")
        else:
            showMessage(message="3")

    else:
        showMessage(message="2")

else:
    showMessage(message="2")
