# MorseMap decode mystery

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


def text_to_morseCode(message):
    cipher = ""
    for letter in message:
        if letter != " ":
            cipher += MORSE_CODE_DICT[letter] + " "
        else:
            cipher += " "
    return cipher


def morseCode_to_text(message):
    message += " "
    decipher = ""
    citext = ""

    for letter in message:
        if letter != " ":
            i = 0
            citext += letter
        else:
            i += 1

            if i == 2:
                decipher += " "
            else:
                for key, value in MORSE_CODE_DICT.items():
                    if citext == value:
                        decipher += key

                citext = ""

    return decipher


message = "The key is hidden in the old tree."
result = text_to_morseCode(message.upper())
print(result)

message = "- .... .  -.- . -.--  .. ...  .... .. -.. -.. . -.  .. -.  - .... .  --- .-.. -..  - .-. . . .-.-.- "
result = morseCode_to_text(message)
print(result)
