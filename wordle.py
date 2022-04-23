word_list = []

with open("words.rtf","r") as words:
    for word in words:
        if len(word) == 5:
            word_list.append(word)
print(word_list)