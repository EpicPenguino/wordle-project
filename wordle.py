import random
length=5
word_list = []
wrong = []
misplaced = [[] for i in range(length)]
correct = ["_" for i in range(length)]

def word_picker():
    with open("words.rtf","r") as words:
        for word in words:
            word = word.split("\\")[0]
            if len(word) == length:
                word_list.append(word)
    return(random.choice(word_list))

def easy_mode():
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
        if bad:
            continue

        possible_list.append(possible)
    return(possible_list)

def main():
    win=False
    wordle = word_picker()
    while win == False:
        print(easy_mode())
        guess = input("\nEnter your guess ")
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
        print(wrong)
        print(misplaced)
        print(correct)
        if correct == list(wordle):
            win=True
            print("You win")

if __name__ == "__main__":
    main()