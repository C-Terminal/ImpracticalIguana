import sys

print("Welcome to the C-Terminal 'Pig Latin Word Generator'\n")


def vowel_or_consonant(x):
    if (x == 'a' or x == 'e' or
            x == 'i' or x == 'o' or x == 'u'):
        return "Vowel"
    else:
        return "Consonant"

pig_latin_word_complete = str()

while True:
    normal_word = input("\n\nEnter a word to be transformed: (or enter n to quit)\n ")
    if normal_word.lower() == "n":
        break

    else:
        firstLetter = normal_word[0]
        letter_type = vowel_or_consonant(firstLetter)

        if letter_type == "Consonant":
            pig_latin_word_consonant = normal_word[1:] + firstLetter + "ay"
            pig_latin_word_complete = pig_latin_word_consonant
        else:
            pig_latin_word_vowel = normal_word + "way"
            pig_latin_word_complete = pig_latin_word_vowel

        message = f"The word {normal_word} in pig latin is {pig_latin_word_complete}!"
        print(message)

input("\nPress enter to exit")
