import pyttsx3
from pathlib import Path
from os import read
import string
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

def Speechtron(speak, voice):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate+10)
    engine.setProperty('voice', voices[voice].id)
    engine.say(speak)
    engine.runAndWait()

def showMessage(message):
    if message == "2":
        print(Fore.BLACK + Back.RED + " INVALID OPTION ")
        Speechtron(speak="INVALID OPTION", voice=narrator_voice)
    elif message == "3":
        print(Fore.BLACK + Back.RED + " FILE NOT FOUND ")
        Speechtron(speak=" FILE NOT FOUND ", voice=narrator_voice)
    elif message == "4":
        print(Fore.BLACK + Back.RED + " File name already exists ")
        Speechtron(speak="File name already exists", voice=narrator_voice)
    elif message == "5":
        print(Fore.GREEN + "Thank you for using Speechtron.")
        Speechtron(speak="Thank you for using Speechtron.", voice=narrator_voice)

def narrateComplt(count):
    word_count = sum([i.strip(string.punctuation).isalpha() for i in count.split()])
    print(Fore.GREEN + "Narration completed. " + "(" + str(word_count) + " words)")
    Speechtron(speak="Narration completed. " + str(word_count) + "words", voice=narrator_voice)


print(Fore.BLACK + Back.BLUE + " Speechtron v2.2.1 - text to speech narrator. ")
Speechtron(speak="Speechtron - text to speech narrator.", voice=2)

print(Fore.YELLOW + 
'''
Available voices :-

0 - Microsoft David
1 - Microsoft Linda
2 - Microsoft Mark (Default)
3 - Cortana
4 - Microsoft Hazel
5 - Microsoft Catherine
6 - Microsoft Zira
''')
Speechtron(speak="Choose narrator voice", voice=2)
narrator_voice = int(input(Fore.LIGHTYELLOW_EX + "Choose narrator voice: "))

Speechtron(speak="Read file or enter text.", voice=narrator_voice)
usr_option = input(Fore.CYAN + "Read file or enter text ? (r/t): ")

var1 = ['r', 'R', 't', 'T']
while usr_option not in var1:
    showMessage(message="2")
    usr_option = input(Fore.CYAN + "Read file or enter text (r/t): ")

if usr_option.lower() == "t":

    Speechtron(speak="Enter your text for narration", voice=narrator_voice)
    user_input = input(Fore.CYAN + "Enter your text for narration: ")

    word_count = sum([i.strip(string.punctuation).isalpha() for i in user_input.split()])
    saving = "narrating user input. " + user_input + ". narration completed. " + str(word_count) + "words."
    Speechtron(speak=user_input, voice=narrator_voice)

    narrateComplt(count=user_input)
    Speechtron(speak="Do you want to save audio file", voice=narrator_voice)
    save_ask = input(Fore.MAGENTA + "Do you want to save audio file (y/n): ")

    var2 = ['y', 'Y', 'n', 'N']
    while save_ask not in var2:
        showMessage(message="2")
        save_ask = input(Fore.MAGENTA + "Do you want to save audio file (y/n): ")

    if save_ask.lower() == "y":
        Speechtron(speak="Name your file", voice=narrator_voice)
        naming_file = input(Fore.YELLOW + "Name your file: ")

        path_to_file = naming_file + ".mp3"
        path = Path(path_to_file)
        if path.is_file():
            showMessage(message="4")

        engine = pyttsx3.init()
        save_voice = engine.getProperty('voices')
        engine.setProperty('voice', save_voice[narrator_voice].id)
        engine.save_to_file(saving, naming_file + '.mp3')
        engine.runAndWait()
        print(Fore.GREEN + f"{naming_file}.mp3 audio file saved")
        Speechtron(speak=f"{naming_file}.mp3 audio file saved", voice=narrator_voice)
    
    elif save_ask.lower() == "n":
        showMessage(message="5")

elif usr_option.lower() == "r":

    Speechtron(speak="Current folder or browsw file", voice=narrator_voice)
    usr_file_path = input(Fore.CYAN + "Current folder or browse file (c/b): ")

    var3 = ['c', 'C', 'b', 'B']
    while usr_file_path not in var3:
        showMessage(message="2")
        usr_file_path = input(Fore.CYAN + "Current folder or browse file (c/b): ")

    if usr_file_path.lower() == "c":
        Speechtron(speak="Enter file name", voice=narrator_voice)
        c_path = input(Fore.CYAN + "Enter file name: ")

        path_to_file = c_path
        path = Path(path_to_file)

        if path.is_file():
            print(f"Narrating file: {c_path}")
            Speechtron(speak=f"Narrating file: {c_path}", voice=narrator_voice)
            with open(c_path, 'rb') as file:
                reading_file1 = file.read()
                #converting bytes to string, because some text might be in bytes when copy paste.
                narrate = str(reading_file1, 'UTF-8')
                print(Fore.YELLOW + narrate)
                word_count = sum([i.strip(string.punctuation).isalpha() for i in narrate.split()])
                savefile = f"narrating file: {c_path}. " + narrate + " Narration completed. " + str(word_count) + "words."
            Speechtron(speak=narrate, voice=narrator_voice)

            narrateComplt(count=narrate)
            Speechtron(speak="Do you want to save audio file", voice=narrator_voice)
            save_ask = input(Fore.MAGENTA + "Do you want to save audio file (y/n): ")

            var2 = ['y', 'Y', 'n', 'N']
            while save_ask not in var2:
                showMessage(message="2")
                save_ask = input(Fore.MAGENTA + "Do you want to save audio file (y/n): ")

            if save_ask.lower() == "y":
                Speechtron(speak="Name your file", voice=narrator_voice)
                naming_file = input(Fore.YELLOW + "Name your file: ")

                path_to_file = naming_file + ".mp3"
                path = Path(path_to_file)
                if path.is_file():
                    showMessage(message="4")

                engine = pyttsx3.init()
                save_voice = engine.getProperty('voices')
                engine.setProperty('voice', save_voice[narrator_voice].id)
                engine.save_to_file(savefile, naming_file + ".mp3")
                engine.runAndWait()
                print(Fore.GREEN + f"{naming_file}.mp3 audio file saved")
                Speechtron(speak=f"{naming_file}.mp3 audio file saved", voice=narrator_voice)

            elif save_ask.lower() == "n":
                showMessage(message="5")

        else:
            showMessage(message="3")

    elif usr_file_path.lower() == "b":

        #tkinter file dialog to browse file
        browse_file = askopenfile(mode='r', filetypes=[('File types speechtron can read', '*.*')])
        if browse_file is not None:
            reading_file = browse_file.read()

        print(Fore.CYAN + "Narrating user file")
        Speechtron(speak="Narrating user file", voice=narrator_voice)

        #converting bytes to string, because some text might be in bytes when copy paste.
        #narrate = str(browse_file, 'UTF-8')
        print(Fore.YELLOW + reading_file)
        word_count = sum([i.strip(string.punctuation).isalpha() for i in reading_file.split()])
        savefile = "narrating user file. " + reading_file + " Narration completed. " + str(word_count) + "words."
        Speechtron(speak=reading_file, voice=narrator_voice)
        narrateComplt(count=reading_file)
        Speechtron(speak="Do you want to save audio file", voice=narrator_voice)
        save_ask = input(Fore.MAGENTA + "Do you want to save audio file (y/n): ")

        var2 = ['y', 'Y', 'n', 'N']
        while save_ask not in var2:
            showMessage(message="2")
            save_ask = input(Fore.MAGENTA + "Do you want to save audio file (y/n): ")

        if save_ask.lower() == "y":
            Speechtron(speak="Name your file", voice=narrator_voice)
            naming_file = input(Fore.CYAN + "Name your file: ")

            path_to_file = naming_file + ".mp3"
            path = Path(path_to_file)
            if path.is_file():
                showMessage(message="4")

            engine = pyttsx3.init()
            save_voice = engine.getProperty('voices')
            engine.setProperty('voice', save_voice[narrator_voice].id)
            engine.save_to_file(savefile, naming_file + ".mp3")
            engine.runAndWait()
            print(Fore.GREEN + f"{naming_file}.mp3 audio file saved")
            Speechtron(speak=f"{naming_file}.mp3 audio file saved", voice=narrator_voice)

        elif save_ask.lower() == "n":
            showMessage(message="5")
