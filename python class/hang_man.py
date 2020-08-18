#### HANGMAN
## DECLARE FILENAME AND OPEN FILE FOR READING
file_name = "words.txt"
file = open(file_name, "r")

## READ FILE AND SPLIT INTO INDIVIDUAL WORDS
data = file.read().split(',')

## IMPORT THE RANDOM MODULE FOR RANDOM VALUE SELECTIONS
import random

## SELECT A RANDOM CHOICE FROM THE LIST OF WORDS READ FROM THE FILE
selected_word = random.choice(data)

print("I have selected a word")

## CREATE A PLACE HOLDER TO HOLD SUCCESSFULLY GUESSED CHARACTERS
guessed_chars_list = []

## DECLARE THE MAXIMUM NUMBER OF TURNS POSSIBLE
turns = 5

## WHILE LOOP IS DECLARED WITH TURNS TO LIMIT NUMBER OF TURNS A USER HAS
while turns:
    
## COLLECT GUESSED WORD FROM USER
    guessed_char = input("Please guess a char : ")

## CHECK IF CHARACTER GUESSED BY USER IS IN THE WORD THAT HAS BEE SELECTED BY THE COMPUTER
    if guessed_char in selected_word:

        ##  IF CHAR IS GUESSED RIGHT THEN ADD THE CHAR TO THE LIST OF SUCCESSFULLY GUESSED CHARS
        guessed_chars_list.append(guessed_char)
    else:
        ##  IF CHAR IS GUESSED WRONG THEN REDUCE NUMBER OF TURNS
        turns -= 1

    for character in selected_word:

        ## PRINT CHARACTER IF IT HAS BEEN GUESSED CORRECTLY
        if character in guessed_chars_list:
            print(character, end ="")
        else:
        ## PRINT DASH IF IT WAS GUESSED WRONG
            print("_", end = "")
    
    print()
    ## PRINT NUMBER OF REMAINING TURNS LEFT
    print(f"You have {turns} tries left..!!!")

    ## CHECK IF ALL CHARACTERS OF THE SELECTED WORD HAVE BEEN GUESSED CORRECTLY, AND IF SO END THE PROGRAM
    if set(guessed_chars_list) == set(selected_word):
        print("Congrats!!!")
        break 