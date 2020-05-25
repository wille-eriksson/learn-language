from googletrans import Translator
from spellchecker import SpellChecker
import random as rand

def add_words():
    spell = SpellChecker(language=u'es')
    translator = Translator()

    f = open('/Users/willeeriksson/Documents/Programmering/learnspanish/wordlists/spanish.txt','a')

    print("Enter word(s) to add. Enter ! when you are done.")

    while True:
        word = str(input()).lower()
        if word == '!': break

        trans = translator.translate(word, dest='en',src='es').extra_data['all-translations']

        if trans == None:
            print(word.capitalize() + " does not seem to be in the dictionary.")

            candidates = spell.candidates(word)
            if len(candidates) > 0:
                print("Here are some suggestions: " + ", ".join(candidates) + ".")
            continue

        all_trans = []

        for wc in trans:
            for w in wc[1]:
                all_trans.append(w)

        f.write(word + '->')

        for w in all_trans[:-1]:
            f.write(w + ",")

        f.write(all_trans[-1] + '\n')

        print("Translation: " + all_trans[0].capitalize())
        print("Other translations include: " + ", ".join(all_trans[1:]) + "." + "\n")

    f.close()

def delete_words():
    print("Enter word(s) to delete. Enter ! when you are done.")

    while True:
        word = str(input()).lower()

        if word == '!': break

        with open('/Users/willeeriksson/Documents/Programmering/learnspanish/wordlists/spanish.txt','r') as f:
            lines = f.readlines()

        for line in lines:
            if line.strip("\n").split("->")[0] == word:
                line_to_delete = line.strip("\n")

        with open('/Users/willeeriksson/Documents/Programmering/learnspanish/wordlists/spanish.txt', "w") as f:
            for line in lines:
                if line.strip("\n") != line_to_delete:
                    f.write(line)

    f.close()

def quiz():
    print("How many words do you want for your quiz?")
    size = int(input())

    f = open('/Users/willeeriksson/Documents/Programmering/learnspanish/wordlists/spanish.txt','a')

    words = []
    translations = {}

    with open('/Users/willeeriksson/Documents/Programmering/learnspanish/wordlists/spanish.txt','r') as f:
        lines = f.readlines()

    for line in lines:
        word, trans = line.strip("\n").split("->")
        all_trans = trans.split(",")
        words.append(word)
        translations.update( {word : all_trans} )

    rand.shuffle(words)
    words = words[:size]

    size = min(size,len(words))
    round = 0

    while len(words)>0:
        missed = []
        round += 1

        print("Round %d" % round)

        for word in words:
            trans = translations[word]
            print(word.capitalize())
            ans = str(input()).lower()
            print()

            if ans == "!": break

            if ans in trans:
                print("Correct!")
                trans.remove(ans)
                if len(trans) > 0: print("Other translations include: " + ", ".join(trans) + "." + "\n")
                else: print()
            else:
                missed.append(word)
                print("Wrong. Correct answers: " + ", ".join(trans) + "." + "\n")
        rand.shuffle(missed)
        words = missed

    print("You completed the quiz in %d rounds!\n" % round)

def clear_words():
    print("Are you sure you want to clear all words? (Y/N)")
    while True:
        ans = str(input()).capitalize()
        if ans == "Y":
            f = open('/Users/willeeriksson/Documents/Programmering/learnspanish/wordlists/spanish.txt', "w")
            f.write("")
            break
        elif ans == "N":
            break

def translate():
    translator = Translator()
    spell = SpellChecker(language=u'es')

    print("Enter word to translate. Enter ! when you are done.")

    #wordclasses = ['noun','verb','adjective','adverb','pronoun','preposition','conjunction','determiner','exclamation']

    #while True:

    # find those words that may be misspelled
    word = str(input()).lower()
    misspelled = spell.unknown([word])
    if len(misspelled) != 0:
        candidates = spell.candidates(word)
        s = ''
        for cand in candidates:
            s += cand + ", "
        s = s[:-2]
        print("The word was not found. Suggestions: " + s)

    trans = translator.translate(word, dest='en',src='es').extra_data['all-translations']


def main():
    while True:
        print("What do you want to do? \n Add words : (A) \n Delete words : (D) \n Clear words (C) \n Quiz : (Q) \n Exit : (E)")
        action = str(input()).capitalize()

        if action == "A":
            add_words()
        elif action == "C":
            clear_words()
        elif action == "D":
            delete_words()
        elif action == "Q":
            quiz()
        elif action == "T":
            translate()
        elif action == "E":
            break
        else:
            print("Invalid action")

if __name__ == '__main__':
    main()
