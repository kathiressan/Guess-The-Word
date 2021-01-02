from __future__ import print_function
''' This module allows the use of a second parameter in the
    print() function. The second parameter we used was end=""
'''
import random
''' This module contains a number of random number number
    generators which will be used in the program to select
    a random word from the list words
'''

WordList = ['artist', 'breeze', 'circle', 'decent', 'enroll', 'filthy', 'growth', 'honest', 'invest',
            'kernel', 'letter', 'narrow', 'meteor', 'policy', 'pursue', 'roster', 'runway', 'scheme',
            'ripple', 'toddle', 'wobbly', 'zeroes']

Repeat = 'Y'  # As long as this is 'Y', the loop below will repeat but if the user enters 'N', the loop will stop

while Repeat == 'Y':
    
    ''' Everytime the loop restarts, the variable must be set to its orginal values
        to prevent the next hangman game from using the previous variable values
    '''
    MissLetter = []
    a = 0
    b = 1
    c = 0
    GuessCounter = 1

    '''
    The code below selects a random number from 0 to 21 (there are 22 words in the wordlist),
    then the word with the randomized number will be selected for play
    '''
    i = random.randint(0, 21)               
    ChosenWord = str.upper(WordList[i])     
    SplitWord = list(ChosenWord)
    
    y = [] # There is no spesific reason as to why the array is named y. This array will be used to insert the correct letters by the user

    # Places the number of underscores which is equal to the length of the word in an array
    for x in SplitWord:
        y.append("_")

    # Prints "Word:"

    print("Word:", end="")

    # The loop runs 5 times for 5 guesses

    while b < 6:

        # This loop prints the 6 underscores at first and the correct guesses starting from the second run onwards

        while a < 6:
            print(y[a], end=" ") # The end=" " prints the next print statement on the same line
            a = a + 1
        UserInput = input("\nEnter your guess letter #" + str(GuessCounter) + ": >> ") # Python 3 doesn't use raw_input

        UserInput = UserInput.upper()  # This allows user to input a lowercase or uppercase letter/word
        b = b + 1
        GuessCounter = GuessCounter + 1
        # End of loop

        # Reusing the variables for the next loop
        a = 0
        c = 0
        # End

        # This loops checks if the letter entered is correct

        while a < 6:

            if UserInput == SplitWord[a]:
                y[a] = UserInput
            elif UserInput != SplitWord[a]:
                c = c + 1  # The c here will be used in the next part of the code below
            a = a + 1

        Test = "".join(y) # This function combines all the lists in the array to become 1 word
        
        '''
        The if statement below removes 2 guesses if the user guesses the wrong word earlier
        This is the optional part in the question given
        '''
        if len(UserInput) > 1 and UserInput != ChosenWord: 
            b = b + 2
            
        '''
        The if statement below will run when the user inputs a single character or letter
        '''
        if len(UserInput) <= 1 or UserInput != ChosenWord:
            if Test != ChosenWord:
                if c == 6:  # If this condition is true, it means that the letter inputed by the user is wrong and will be stored in MissLetter[]
                    MissLetter.append(UserInput)

                print("Misses: ", end="")   # This will print the misses  
                for letter in MissLetter:
                    print(letter, end=" ")

                print("\nWord:", end=" ")   # The \n is used to counteract the end=""
                a = 0
                while a < 6:
                    print(y[a], end=" ")    # This will print the underscores representing unsolved letters and solved letters
                    a = a + 1
            else:
                print("You Win!")           # The user wins if the all letters are guessed before the number of gusses reaches 5
                b = 6
        else:
            if len(UserInput) > 1 or Test == ChosenWord:        # The user wins if the length of the word is > 1 and is the same as the word in play
                if UserInput == ChosenWord or Test == ChosenWord:
                    print("\nYou Win!")
                    b = 6

    Test = "".join(y)   # This if statement is for when the user already used 5 guesses and now has to guess the whole word
    if UserInput != ChosenWord:
        if Test != ChosenWord:
            FinalAnswer = input("\nEnter your guess word: >> ")
            FinalAnswer = str.upper(FinalAnswer)
            if FinalAnswer == ChosenWord:
                print("You win!")
            else:
                print("You lose!")

    Repeat = input("Play again? Y/N ") # Asks the user if they want to play again 
    Repeat = str.upper(Repeat) # Allows the user to enter Y or N is uppercase or lowercase










