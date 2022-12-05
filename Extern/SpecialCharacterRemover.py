from unidecode import unidecode
# TODO: insert from the user the correct dictionary and checks if it is valid
fd = open("../Dictionaries/dictionaryRO.txt", "rt", encoding="utf8")
fdest = open("../Dictionaries/dictionary.txt", "wt", encoding="utf8")
for word in fd:
    if len(word) <= 9:
        fdest.write(unidecode(word))