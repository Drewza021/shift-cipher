import collections  # import functions from collections module


def shift():
    global new_message  # make new_message usable within the function
    for character in message:  # each loop, set "character" to next character in message string

        if character == " ":  # execute if character is space
            new_character = character  # leave spaces as they are

        elif character in alphabet:  # execute if character is lowercase letter
            position = alphabet.find(character)  # find position of letter in alphabet string
            new_position = (position + key) % len(alphabet)  # add key value to position of letter to get new position
            new_character = alphabet[new_position]  # set new character to character of above position

        elif character in alphabet.upper():  # same as if statement above, with uppercase letters
            position = alphabet.upper().find(character)
            new_position = (position + key) % len(alphabet)
            new_character = alphabet.upper()[new_position]

        elif character in digits:  # execute if character is digit
            position = digits.find(character)  # find position of digit in digit string
            new_position = (position + key) % len(digits)  # add key value to position of digit to get new position
            new_character = digits[new_position]  # set new character to character of above position

        elif character in special:  # execute if character is within string of special characters
            position = special.find(character)  # find position of character in special string
            new_position = (position + key) % len(special)  # add key value to position of letter to get new position
            new_character = special[new_position]  # set new character to character of above position

        else:  # execute if character could not be found in character strings
            new_character = character  # leave character
            print(character + " could not be processed")

        new_message += new_character  # add processed character to "new_message" string


# character strings
alphabet = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"  # all special characters on US keyboard, ordered according to ASCII
new_message = ""  # declare "new_message" so that it can be updated later
message = ""  # declare "message" so that it can be updated later
key = ""  # declare "key" to avoid error message if it's never set by user

algorithm = input("Input \"e\" (encrypt) or \"d\" (decrypt): ").lower()  # offer options of encryption or decryption

if algorithm == "e":  # execute if user chooses encryption
    message = input("Input message to be encrypted: ")  # allow user to input message
    key = int(input("Input key: "))  # allow user to input key
elif algorithm == "d":
    message = input("Input message to be decrypted: ")  # allow user to input ciphertext
    has_key = input("Do you have a key (y/n)? ").lower()  # ask user if they have a key

    if has_key == "y":  # execute if user has key
        key = int(input("Input key: ")) * -1  # ask for key, multiply by -1 to shift backwards instead of forwards
    elif has_key == "n":  # execute if user does not have key
        key = "unknown"  # set key to "unknown" so it can be checked later
        print("Note: cryptanalysis decryption is most effective with longer messages")

else:  # execute if user inputs something other than "y" or "n"
    print("Invalid input")

if key != "unknown":  # execute if user input a valid key for either encryption or decryption
    shift()  # executes shift function defined above
    print()
    print(new_message)  # prints processed message

elif key == "unknown" and algorithm == "d":  # execute if user chooses decryption and has no key

    # a version of the message with only lowercase letters must be generated to find most frequent letter
    only_letters = ""
    for j in message.lower():  # each loop, set "j" to next character in "message" string, converted to lowercase
        if j in alphabet:  # execute if "j" is a letter
            only_letters += j  # add "j" to "only_letters" string

    print()
    print("Likely messages:")

    for k in range(0, 5):  # loop 5 times to generate 5 most likely messages
        # retrieve [k]th most frequent letter in "only_letters"
        kth_common, redundant = collections.Counter(only_letters).most_common()[k]
        # subtract position of e from position of "kth_common" to calculate key
        key = ((alphabet.find(kth_common) - alphabet.find("e")) % len(alphabet)) * -1

        shift()  # shift letters according to this calculated key
        print()
        # print decrypted message and key used
        print(new_message + " (key: " + str(key * -1) + " or " + str((26 + key) * -1) + ")")
        new_message = ""  # reset "new_message" so it can be used again for next message decryption
    # this will only work as intended if "e" is one of the 5 most frequent letters

    print()
    # provide option for brute force decryption in case message did not appear
    request_brute_force = input("If the message did not appear, you can execute brute force decryption "
                                "(input \"r\" to run, any other input to end) ")
    print()

    if request_brute_force.lower() == "r":  # execute if user decided to execute brute force decryption
        for key in range(1, 27):  # each loop increase key by 1 up to 26
            key *= -1  # multiply key by -1 to shift backwards
            shift()  # execute shift function
            print()
            # print decrypted message and key used
            print(new_message + " (key: " + str(key * -1) + " or " + str((26 + key) * -1) + ")")
            new_message = ""  # reset "new_message" so it can be used for next message decryption
    else:
        pass

elif key == "":  # if key is never set by user then do nothing
    pass

'''
test decryption message:
    Xli uymgo: fvsar jsb nyqtw sziv xli pedc hsk<
    Kyv Trvjri tzgyvi nrj jlggfjvucp wfidlcrkvu sp Alczlj Trvjri ze rggifozdrkvcp 877 ST reu zemfcmvu jyzwkzex vrty cvkkvi fw kyv rcgyrsvk kyivv gcrtvj wfinriu kf tivrkv tzgyvikvok
'''

# Caesar Cipher by Drew
