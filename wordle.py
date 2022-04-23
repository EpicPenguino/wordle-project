length=5
word_list = []
wrong = []
misplaced = [[]]*length
correct = ["_"]*length
with open("words.rtf","r") as words:
    for word in words:
        word = word.split("\\")[0]
        if len(word) == length:
            word_list.append(word)
print(word_list)
wordle = "hello"

guess = input("Enter your guess ")
for letter in guess:
    if letter in wordle:
        spot = guess.index(letter)
        if spot == wordle.index(letter):
            correct[spot] = letter
        else:
            misplaced[spot].append(letter)
    else:
        wrong.append(letter)
print(wrong)
print(misplaced)
print(correct)