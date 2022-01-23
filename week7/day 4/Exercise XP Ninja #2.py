# Exercise 1 : What’s Your Name ?
# Instructions
# Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
# middle_name should be optional, if it’s omitted by the user, the name returned should only contain the first and the last name.
# For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.


def get_full_name():
    first_name = input("Enter first name:  ")
    optional_mid = input(
        "its optional chocie if you have a middel name  (y/n)")
    if optional_mid.lower == 'n':
        pass
    else:
        middel_name = input("Enter middle name:  ")
    last_name = input("Entre last name:  ")
    print(f"hi {first_name} {middel_name} {last_name}")


get_full_name()


# Exercise 2 : From English To Morse
# Instructions
# Write a function that converts English text to morse code and another one that does the opposite.
# Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.


MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            cipher += MORSE_CODE_DICT[letter] + ' '
        else:

            cipher += ' '

    return cipher


def decrypt(message):

    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        if (letter != ' '):

            i = 0

            citext += letter

        else:

            i += 1

            if i == 2:

                decipher += ' '
            else:

                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                              .values()).index(citext)]
                citext = ''

    return decipher


def main():
    message = "pavel bandurin"
    result = encrypt(message.upper())
    print(result)

    message = ".--. .- ...- . .-..  -... .- -. -.. ..- .-. .. -."
    result = decrypt(message)
    print(result)


if __name__ == '__main__':
    main()
