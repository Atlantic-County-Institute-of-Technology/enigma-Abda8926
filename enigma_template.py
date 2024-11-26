# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: Youssief Abdalla
# created: 11.18.2024
# last update:  11.18.2024
import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"

def genmsg(text, k):
    newmsg = ""
    for i in range(len(text)):
        try:
            letter = alphabet[(alphabet.index(text[i]) % 26 + k) % 26]
        except ValueError:
            letter = text[i]
        newmsg += letter
    return newmsg

# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message():
    msg = str(input("Input Message here: ")).lower()
    key = input("Input the rotational cipher key: (Press enter for random value)")
    if key == "":
        key = random.randint(0, 25)
    try:
        key = int(key)
    except ValueError:
        print("You did not enter a valid value, key being randomized...")
        key = random.randint(0, 25)
    newmsg = genmsg(msg, key)
    print(f"Used key of {key} your new message is : {newmsg}")


# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    newmsg = ""
    fileFound = False
    while fileFound is False:
        filen = str(input("What is the name of the file you want to encode?"))
        try:
            file = open(filen, 'r')
            filetxt = file.read().lower()
            print(filetxt)
            fileFound = True
        except FileNotFoundError:
            print("That file does not exist.")
            fileFound = False
    key = input("Input the rotational cipher key: (Press enter for random value)")
    if key == "":
        key = random.randint(0, 25)
    try:
        key = int(key)
    except ValueError:
        print("You did not enter a valid value, key being randomized...")
        key = random.randint(0, 25)
    newmsg = genmsg(filetxt, key)
    file.close()
    print(f"Encoded with a key of {key}!")
    choice = int(input("Choose an option: \n"
                       "1. Overwrite original file.\n"
                       "2. Write new file."))
    if choice == 1:
        file = open(filen, "w")
        file.write(newmsg)
    if choice == 2:
        randomvalue = str(random.randint(1, 100))
        file = open(f"encoded + {randomvalue} " + filen, "x")
        file.write(newmsg)


# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    newmsg = ""
    fileFound = False
    while fileFound is False:
        filen = str(input("What is the name of the file you want to encode?"))
        try:
            file = open(filen, 'r')
            filetxt = file.read().lower()
            fileFound = True
        except FileNotFoundError:
            print("That file does not exist.")
            fileFound = False
    key = input("If you know the key, enter it. If not, press enter.")
    if key == "":
        decode_unknown_key(filetxt)
        return
    try:
        key = int(key)
    except ValueError:
        decode_unknown_key(filetxt)
        return
    for i in range(len(filetxt)):
        try:
            letter = alphabet[(alphabet.index(filetxt[i]) % 26 - key) % 26]
        except ValueError:
            letter = filetxt[i]
        newmsg += letter
    print(newmsg)

# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filename):
    print("UNKNOWN!")
    for key in range(26):
        newmsg = ""
        for i in range(len(filename)):
            try:
                letter = alphabet[(alphabet.index(filename[i]) % 26 - key) % 26]
            except ValueError:
                letter = filename[i]
            newmsg += letter
        print(f"KEY #{key}: {newmsg} is key")


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
