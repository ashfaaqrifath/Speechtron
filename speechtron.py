import pyttsx3
from pathlib import Path
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

def Speechtron(speak):
    engine = pyttsx3.init()
    engine.say(speak)
    engine.runAndWait()

print(Fore.BLACK + Back.BLUE + " Speechtron basic text narrator. Read file or enter text for narration. ")
Speechtron("Speechtron basic text narrator. Read file or enter text for narration.")

usr_option = input(Fore.CYAN + "Read file or enter text (r/t)? ")

if usr_option.lower() == "t":
    Speechtron("Enter your text for narration")
    user_input = input(Fore.YELLOW + "Enter your text for narration: ")
    saving = "narrating user input. " + user_input + ". narration completed"

    Speechtron(user_input)

    print(Fore.GREEN + "Narration completed")
    Speechtron("Narration completed")

    Speechtron("Do you want to save audio file")
    save_ask = input("Do you want to save audio file (y/n): ")

    if save_ask.lower() == "y":
        Speechtron("Name your file")
        naming_file = input("Name your file: ")
        engine = pyttsx3.init()
        engine.save_to_file(saving, naming_file + '.mp3')
        engine.runAndWait()
        print("Audio file saved")
        Speechtron("Audio file saved")

elif usr_option.lower() == "r":
    Speechtron("Current path or absolute path")
    usr_file_path = input(Fore.CYAN + "Current path or absolute path (c/a)? ")

    if usr_file_path.lower() == "c":
        Speechtron("Enter file name")
        c_path = input(Fore.YELLOW + "Enter file name: ")

        path_to_file = c_path
        path = Path(path_to_file)

        if path.is_file():
            print(f"Narrating file {c_path}")
            Speechtron(f"Narrating file {c_path}")
            with open(c_path, 'rb') as file:
                reading_file1 = file.read()
                #converting bytes to string, because some text might be in bytes when copy paste.
                narrate = str(reading_file1, 'UTF-8')
                print(narrate)
                savefile = f"narrating file {c_path}. " + narrate + " Narration completed"
            Speechtron(narrate)

            print(Fore.GREEN + "Narration completed")
            Speechtron("Narration completed")

            Speechtron("Do you want to save audio file")
            save_ask = input("Do you want to save audio file (y/n): ")

            if save_ask.lower() == "y":
                Speechtron("Name your file")
                naming_file = input("Name your file: ")
                engine = pyttsx3.init()
                engine.save_to_file(savefile, naming_file + ".mp3")
                engine.runAndWait()
                print("Audio file saved")
                Speechtron("Audio file saved")
        else:
            print(Fore.BLACK + Back.RED + " FILE NOT FOUND ")
            Speechtron(" FILE NOT FOUND ")

    elif usr_file_path.lower() == "a":
        Speechtron("Enter file path")
        a_path = input(Fore.YELLOW + "Enter file path: ")

        path_to_file = a_path
        path = Path(path_to_file)

        if path.is_file():
            print(f"Narrating file {a_path}")
            Speechtron(f"Narrating file {a_path}")
            with open(a_path, 'rb') as file:
                reading_file2 = file.read()
                # converting bytes to string, because some text might be in bytes when copy paste.
                narrate = str(reading_file2, 'UTF-8')
                print(narrate)
                savefile = f"narrating file {a_path}. " + narrate + " Narration completed"
            Speechtron(narrate)

            print(Fore.GREEN + "Narration completed")
            Speechtron("Narration completed")

            Speechtron("Do you want to save audio file")
            save_ask = input("Do you want to save audio file (y/n): ")

            if save_ask.lower() == "y":
                Speechtron("Name your file")
                naming_file = input("Name your file: ")
                engine = pyttsx3.init()
                engine.save_to_file(savefile, naming_file + ".mp3")
                engine.runAndWait()
                print("Audio file saved")
                Speechtron("Audio file saved")
        else:
            print(Fore.BLACK + Back.RED + " FILE NOT FOUND ")
            Speechtron(" FILE NOT FOUND ")

    else:
        print(Fore.BLACK + Back.RED + " INVALID OPTION ")
        Speechtron("INVALID OPTION")

else:
    print(Fore.BLACK + Back.RED + " INVALID OPTION ")
    Speechtron("INVALID OPTION")
