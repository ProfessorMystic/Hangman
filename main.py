import dictionary  # imports dictionary file containing word list and hangman imagery


# function for playing again
def restart():
    user_input = input("Would you like to play again? Y/N: ").upper()
    if user_input == "Y":
        game()
    elif user_input == "N":
        exit()
    else:
        print("Invalid input\n")
        restart()  # call function again


# function for the main game
def game():
    attempt = 0  # will be sent to tries function, with each incorrect answer incrementing attempt += 1
    word = dictionary.getword()  # grabs word from dictionary file
    line = []  # initialized to append underscores, representing blank spaces needed to fill out word
    for _ in word:
        line.append("_")
    print("\nWelcome to Hangman!\n")
    while attempt < 7:
        dictionary.tries(attempt)  # prints pole and body
        print("\n" + ' '.join(line))  # prints line
        ans = input("\nGuess a letter or word, and try to fill in the blanks: ").upper()  # user input is capitalized
        if ans == "":
            print("No input detected.")
        elif word.find(ans) == -1:  # implies that user answer length = 1 & DOES NOT exist in word
            print(ans + " is not located")
            attempt += 1
        elif len(ans) == 1:  # user answer length = 1 and DOES exist in word
            for idx, i in enumerate(word):
                if i == ans:
                    line[idx] = ans
        elif ans == word:  # user guesses answer correctly; wins game
            line = word
            dictionary.tries(attempt)
            print("\n" + ' '.join(line) + "\nCongratulations, you guessed the word! The word was: " + word)
            restart()
        else:  # user guesses answer incorrectly; attempt += 1
            print("Oops, " + ans + " is not the word. Don't answer too hastily!")
            attempt += 1
        if str(line).find("_") == -1:  # checks to see if any underscore is remaining; if not then user wins
            dictionary.tries(attempt)
            print("\n" + ' '.join(line) + "\nCongratulations, you guessed the word! The word was: " + word)
            restart()
    dictionary.tries(attempt)  # implies that full body has been constructed and hung; game over
    print("\n" + ' '.join(line) + "\n\nYou've been hung! The word was: " + word)
    restart()  # calls restart function to ask if user wants to play again


game()  # program runs game
