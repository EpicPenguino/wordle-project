import random
length=5
word_list = []
wrong = []
misplaced = [[] for i in range(length)]
correct = ["_" for i in range(length)]
win=False

with open("words.rtf","r") as words:
    for word in words:
        word = word.split("\\")[0]
        if len(word) == length:
            word_list.append(word)
wordle = (random.choice(word_list))

while win == False:
    guess = input("Enter your guess ")
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