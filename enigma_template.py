# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: Youssief Abdalla
# created: 11.18.2024
# last update:  11.26.2024
import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"

def findfile():
    # function that finds file to use in encode/decode
    file_found = False
    while file_found is False:
        filen = str(input("What is the name of the file you want to use?"))
        try:
            file = open(filen, 'r')
            filetxt = file.read().lower()
            file.close()
            return filetxt, filen
        except FileNotFoundError:
            print("That file does not exist.")
    # loops until file is valid, then returns the file's text and name


def keychoice():
    # asks for a key, if key is blank or not valid, randomizes the value.
    key = input("Input the rotational cipher key: (Press enter for random value)")
    if key == "":
        key = random.randint(0, 25)
    try:
        key = int(key)
    except ValueError:
        print("You did not enter a valid value, key being randomized...")
        key = random.randint(0, 25)
    return key
    # returns the key value



def genmsg(text, k):
    newmsg = ""
    for i in range(len(text)):
        try:
            letter = alphabet[(alphabet.index(text[i]) % 26 + k) % 26]
        except ValueError:
            letter = text[i]
        newmsg += letter
    return newmsg
    # creates the new message for an encode.


# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message():
    msg = str(input("Input Message here: ")).lower()
    key = keychoice()
    newmsg = genmsg(msg, key)
    print(f"Used key of {key} your new message is : {newmsg}")
    # informs user of what the key is and displays the message
    choice = str(input("Do you want to write this message to a new file? (y/N)")).lower()
    if choice == "y":
        inputval = False
        while inputval is False:
            try:
                filename = str(input("What would you like to name the file?"))
                file = open(filename, "x")
                file.write(newmsg)
                file.close()
                print("File created.")
                inputval = True
            except FileNotFoundError:
                print("File name can not be blank or already exists")
            except FileExistsError:
                print("File name can not be blank or already exists")
                # if the user wants to create a file, ask them for a name and then create the file.
    elif choice != "y":
        pass


# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    filetxt, filen = findfile()
    key = keychoice()
    print(f"Encoded with a key of {key}!")
    inputval = True
    while inputval is True:
        # asks if the user wants to overwrite a file or create a new one
        try:
            choice = int(input("Choose an option: \n"
                               "1. Overwrite original file.\n"
                               "2. Write new file."))
            if choice == 1:
                inputval = False
                file = open(filen, "w")
                file.write(genmsg(filetxt, key))
                file.close()
                print("File rewritten.")
                # opens the file, overwrites the text, closes file
            if choice == 2:
                inputval = False
                inputval2 = True
                while inputval2 is True:
                    try:
                        filename = str(input("What would you like to name the file?"))
                        file = open(filename, "x")
                        # asks user for file name and creates the file
                        file.write(genmsg(filetxt, key))
                        file.close()
                        print("File written.")
                        inputval2 = False
                    except FileNotFoundError:
                        print("File cannot have blank or existing name.")
                    except FileExistsError:
                        print("File cannot have blank or existing name.")
                # creates file, writes in file, closes file
        except ValueError:
            print("Invalid Choice. Please try again.")
            inputval = True

# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    newmsg = ""
    filetxt, filen = findfile()
    key = input("If you know the key, enter it. If not, press enter.")
    if key == "":
        decode_unknown_key(filetxt)
        return
    try:
        key = int(key)
    except ValueError:
        decode_unknown_key(filetxt)
        return
    # asks if the user knows the key, if not, it runs the unknown key function.
    for i in range(len(filetxt)):
        try:
            letter = alphabet[(alphabet.index(filetxt[i]) % 26 - key) % 26]
        except ValueError:
            letter = filetxt[i]
        newmsg += letter
    # separate from the genmsg() function because decoding uses subtraction
    print(newmsg)
    # prints new, decoded mesasage


# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filetext):
    print("UNKNOWN KEY... GENERATING ALL POSSIBLE VALUES...")
    for key in range(26):
        # loops 26 times to account for all possible keys
        newmsg = ""
        for i in range(len(filetext)):
            try:
                letter = alphabet[(alphabet.index(filetext[i]) % 26 - key) % 26]
            except ValueError:
                letter = filetext[i]
            newmsg += letter
        print(f"KEY #{key}: {newmsg}")
    # runs the decode message code and prints after each key is tried.


# main method declaration
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Exit.")

        selection = input("Choose an option:")

        if selection == "1":
            encode_message()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")


# runs on program start
if __name__ == "__main__":
    main()
