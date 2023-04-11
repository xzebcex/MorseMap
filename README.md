## **MorseMap decode mystery**
## Description
This is a Python script that can convert text to Morse code and vice versa using a dictionary containing the Morse code equivalent of each letter.

Table of Contents

1.	[Morse Code Dictionary](#morse_code_dict)
2.	[Functions](#function)
3.	[How to Use](#how_to_use)
4.	[Example](#example)
5.	[License](#license)
6.	[How to Contribute](#how_to_contribute)
7.	[Additional Points](#additional_points)
8.	[Conclusion](conclusion)

## Morse Code Dictionary <a name="morse_code_dict"></a>
Morse code uses dots and dashes to represent letters and numbers. The script includes a dictionary MORSE_CODE_DICT containing the Morse code equivalent of each letter and some special characters.

## Functions <a name="function"></a>
The script includes two functions:
-	text_to_morseCode(message): This function takes a message as input and returns the message encoded in Morse code.
-	morseCode_to_text(message): This function takes a message in Morse code as input and returns the decoded message.
## How to Use <a name="how_to_use"></a>
-	Clone or download the repository.
-	Open the terminal and navigate to the directory where the script is located.
-	Run the script by typing python morse_map_decode.py.
-	Follow the prompts to either convert text to Morse code or Morse code to text.
## Example <a name="example"></a>
- Output 1:

.... . -.- . -.-- .. ... .... .. -.. -.. . -. .. -. - .... . --- .-.. -.. - .-. . .-.-.- .
Explanation: This is the Morse code equivalent of the message "The key is hidden in the old tree" with spaces between each Morse code letter and an additional gap between words.

- Output 2:
THE KEY IS HIDDEN IN THE OLD TREE.
Explanation: This is the message deciphered from the Morse code seen in Output 1.


## License <a name="license"></a>
MIT License applies.

## How to Contribute <a name="how_to_contribute"></a>
Contributions are not presently required for this code, although they are much welcomed. You may clone the repository and make your own changes if you want to. If you want to share your improvements with the community, submit a pull request.





## Aditional Points <a name="additional_points"></a>
-	Error handling to ensure valid input and handle errors
-	User-friendly interface, such as a graphical user interface (GUI)
-	Support for different languages, not just the English alphabet and common punctuation
-	Speed optimization for more efficient decoding of longer messages
-	Expanded functionality, such as playing Morse code sounds
## Conslusion  <a name="conclusion"></a>
MorseMap decode mystery is a simple Python script that allows you to convert text to Morse code and vice versa. The script makes use of a dictionary containing the Morse code mappings for each letter and number. The text_to_morseCode function takes in a message and returns the Morse code equivalent, while the morseCode_to_text function takes in a Morse code message and returns the text equivalent. This script can be useful for anyone interested in learning Morse code or for communication purposes in situations where verbal communication is not possible. Feel free to modify and improve upon it as needed.
