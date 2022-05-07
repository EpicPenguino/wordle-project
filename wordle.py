import random

# Opens a dictionary text-file and makes a list of every word of a user-inputted length and then returns a random word from that list
# dictionary -> type: string
# length -> type: int
# word_list -> type: list
def word_picker(dictionary,length,word_list):
    with open(dictionary,"r") as words:
        for word in words:
            word = word.split("\\")[0]
            word = word.split("\n")[0]
            if len(word) == length:
                word_list.append(word)
    if len(word_list) == 0:
        print("No possible words that length, please input different length.")
        length = int(input("What word length do you want? "))
        word_picker(dictionary,length,word_list)
        
    return(random.choice(word_list))

# Passes every word in word_list through the hints provided and returns a list of the possible answers
# word_list -> type: list
# wrong -> type: list
# misplaced -> type: list
# correct -> type: list
def easy_mode(word_list,wrong,misplaced,correct):
    possible_list = []
    for possible in word_list:
        bad=False
        for wrong_hint in wrong:
            if wrong_hint in possible:
                bad=True
                break
        if bad:
            continue

        for spot1,letter1 in enumerate(possible):
            if correct[spot1] == "_":
                continue
            if correct[spot1] != letter1:
                bad=True
                break
        if bad:
            continue

        for spotM,letter_list in enumerate(misplaced):
            for letterM in letter_list:
                if letterM not in possible or possible[spotM] == letterM:
                    bad=True
                    break
            if bad:
                break
            continue

        possible_list.append(possible)
    return(possible_list)

# Run the guess through the list of possible answers provided by easy_mode function and returns a boolean of whether it is or is not
# guess -> type: string
# possible_list -> type: list
def hard_mode(guess,possible_list):
    return guess not in possible_list

def main():
    if input("Would you like to play using German words? yes or no: ").lower() == "yes":
        dictionary = "wordlist-german.txt"
    else:
        dictionary = "words.rtf"
    length = int(input("What word length do you want? "))
    easy_enabled = input("Would you like to play with hints mode? yes or no: ").lower() == "yes"
    hard_enabled = input("Would you like to play with hard mode? yes or no: ").lower() == "yes"
    
    # word_list sets up a list to put every word inside of. wrong, misplaced, and correct are the "hint" lists. win is the bool that determines whether to continue the game
    word_list, wrong, misplaced, correct, win = [], [], [[] for i in range(length)], ["_" for i in range(length)], False
    
    wordle = word_picker(dictionary,length,word_list)
    while not win:
        
        possible_list = easy_mode(word_list,wrong,misplaced,correct)
        if easy_enabled:
            print(possible_list)
        
        guess = input("\nEnter your guess: ")
        
        if hard_enabled and hard_mode(guess,possible_list):
            print("Guess does not match hints")
            if guess not in word_list:
                print("Invalid guess")
            continue
        if guess not in word_list:
            print("Invalid guess")
            continue

        wordle2 = wordle[:]
        for spot,letter in enumerate(guess):
            if letter in wordle2:
                if spot == wordle2.index(letter):
                    correct[spot] = letter
                    wordle2 = (wordle2[0:spot] + "_" + wordle2[spot+1:])
                else:
                    if letter not in misplaced[spot]:
                        misplaced[spot].append(letter)
            else:
                if letter not in wrong:
                    wrong.append(letter)
            guess = (guess[0:spot] + "_" + guess[spot+1:])
        wrong.sort()
        print(f"Wrong letters: {wrong}")
        print(f"Misplaced letters: {misplaced}")
        print(f"Correctly positioned letters: {correct}")
        if correct == list(wordle):
            win=True
            print("__     __                    _         _ ")
            print("\ \   / /                   (_)       | |")
            print(" \ \_/ /__  _   _  __      ___ _ __   | |")
            print("  \   / _ \| | | | \ \ /\ / / | '_ \  | |")
            print("   | | (_) | |_| |  \ V  V /| | | | | |_|")
            print("   |_|\___/ \__,_|   \_/\_/ |_|_| |_| (_)")

if __name__ == "__main__":
    main()