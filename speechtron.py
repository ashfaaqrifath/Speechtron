from os import read
import pyttsx3
from pathlib import Path
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
        print("File name already exists")
        Speechtron(speak="File name already exists", voice=narrator_voice)

def narrateComplt(count):
    word_count = sum([i.strip(string.punctuation).isalpha() for i in count.split()])
    print(Fore.GREEN + "Narration completed. " + "(" + str(word_count) + " words)")
    Speechtron(speak="Narration completed. " + str(word_count) + "words", voice=narrator_voice)


print(Fore.BLACK + Back.BLUE + " Speechtron - text to speech narrator.")
Speechtron(speak="Speechtron - text to speech narrator.", voice=0)

print(
'''
Available voices :-
0 - Duncan (Default)
1 - Adriana
2 - Natasha
3 - Gibberish
''')
Speechtron(speak="Choose narrator voice", voice=0)
narrator_voice = int(input("Choose narrator voice: "))

Speechtron(speak="Read file or enter text.", voice=narrator_voice)
usr_option = input(Fore.CYAN + "Read file or enter text (r/t): ")

var1 = ['r', 'R', 't', 'T']
while usr_option not in var1:
    showMessage(message="2")
    usr_option = input(Fore.CYAN + "Read file or enter text (r/t): ")

if usr_option.lower() == "t":

    Speechtron(speak="Enter your text for narration", voice=narrator_voice)
    user_input = input(Fore.YELLOW + "Enter your text for narration: ")
    word_count = sum([i.strip(string.punctuation).isalpha() for i in user_input.split()])
    saving = "narrating user input. " + user_input + ". narration completed. " + str(word_count) + "words."
    Speechtron(speak=user_input, voice=narrator_voice)

    narrateComplt(count=user_input)
    Speechtron(speak="Do you want to save audio file", voice=narrator_voice)
    save_ask = input("Do you want to save audio file (y/n): ")

    var2 = ['y', 'Y', 'n', 'N']
    while save_ask not in var2:
        showMessage(message="2")
        save_ask = input("Do you want to save audio file (y/n): ")

    if save_ask.lower() == "y":
        Speechtron(speak="Name your file", voice=narrator_voice)
        naming_file = input("Name your file: ")

        path_to_file = naming_file + ".mp3"
        path = Path(path_to_file)
        if path.is_file():
            showMessage(message="4")

        engine = pyttsx3.init()
        save_voice = engine.getProperty('voices')
        engine.setProperty('voice', save_voice[narrator_voice].id)
        engine.save_to_file(saving, naming_file + '.mp3')
        engine.runAndWait()
        print(f"{naming_file}.mp3 audio file saved")
        Speechtron(speak=f"{naming_file}.mp3 audio file saved", voice=narrator_voice)

elif usr_option.lower() == "r":

    Speechtron(speak="Current folder or browsw file", voice=narrator_voice)
    usr_file_path = input(Fore.CYAN + "Current folder or browse file (c/b): ")

    var3 = ['c', 'C', 'b', 'B']
    while usr_file_path not in var3:
        showMessage(message="2")
        usr_file_path = input(Fore.CYAN + "Current folder or browse file (c/b): ")

    if usr_file_path.lower() == "c":
        Speechtron(speak="Enter file name", voice=narrator_voice)
        c_path = input(Fore.YELLOW + "Enter file name: ")

        path_to_file = c_path
        path = Path(path_to_file)

        if path.is_file():
            print(f"Narrating file: {c_path}")
            Speechtron(speak=f"Narrating file: {c_path}", voice=narrator_voice)
            with open(c_path, 'rb') as file:
                reading_file1 = file.read()
                #converting bytes to string, because some text might be in bytes when copy paste.
                narrate = str(reading_file1, 'UTF-8')
                print(narrate)
                word_count = sum([i.strip(string.punctuation).isalpha() for i in narrate.split()])
                savefile = f"narrating file: {c_path}. " + narrate + " Narration completed. " + str(word_count) + "words."
            Speechtron(speak=narrate, voice=narrator_voice)

            narrateComplt(count=narrate)
            Speechtron(speak="Do you want to save audio file", voice=narrator_voice)
            save_ask = input("Do you want to save audio file (y/n): ")

            if save_ask.lower() == "y":
                Speechtron(speak="Name your file", voice=narrator_voice)
                naming_file = input("Name your file: ")

                path_to_file = naming_file + ".mp3"
                path = Path(path_to_file)
                if path.is_file():
                    showMessage(message="4")

                engine = pyttsx3.init()
                save_voice = engine.getProperty('voices')
                engine.setProperty('voice', save_voice[narrator_voice].id)
                engine.save_to_file(savefile, naming_file + ".mp3")
                engine.runAndWait()
                print(f"{naming_file}.mp3 audio file saved")
                Speechtron(speak=f"{naming_file}.mp3 audio file saved", voice=narrator_voice)
        else:
            showMessage(message="3")

    elif usr_file_path.lower() == "b":
        
        browse_file = askopenfile(mode='r', filetypes=[('File types speechtron can read', '*.*')])
        if browse_file is not None:
            reading_file = browse_file.read()

        print("Narrating user file")
        Speechtron(speak="Narrating user file", voice=narrator_voice)

        #converting bytes to string, because some text might be in bytes when copy paste.
        #narrate = str(browse_file, 'UTF-8')
        print(reading_file)
        word_count = sum([i.strip(string.punctuation).isalpha() for i in reading_file.split()])
        savefile = "narrating user file. " + reading_file + " Narration completed. " + str(word_count) + "words."
        Speechtron(spaek=reading_file, voice=narrator_voice)
        narrateComplt(count=reading_file)
        Speechtron("Do you want to save audio file")
        save_ask = input("Do you want to save audio file (y/n): ")

        if save_ask.lower() == "y":
            Speechtron(speak="Name your file", voice=narrator_voice)
            naming_file = input("Name your file: ")

            path_to_file = naming_file + ".mp3"
            path = Path(path_to_file)
            if path.is_file():
                showMessage(message="4")

            engine = pyttsx3.init()
            save_voice = engine.getProperty('voices')
            engine.setProperty('voice', save_voice[narrator_voice].id)
            engine.save_to_file(savefile, naming_file + ".mp3")
            engine.runAndWait()
            print(f"{naming_file}.mp3 audio file saved")
            Speechtron(speak=f"{naming_file}.mp3 audio file saved", voice=narrator_voice)
