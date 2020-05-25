import random as rand
import os

def round(round_number, words, translations):
    missed = []
    words_left = len(words)

    if words_left == 0:
        return None

    print("Round %d. \n%d word(s) left." % (round_number,words_left))
    input()
    os.system('clear')

    for word in words:
        print("Round %d \n" % round_number + word.capitalize() )
        trans = translations[word].copy()
        ans = str(input()).lower()

        if ans == "b":
            return None
        elif ans in trans:
            print("\nCorrect!")
            trans.remove(ans)
            if len(trans) > 0: print("Other translations include: " + ", ".join(trans) + "." + "\n")
            else: print()
        else:
            missed.append(word)
            print("\nWrong. Correct answers: " + ", ".join(trans) + "." + "\n")
        input()
        os.system('clear')

    rand.shuffle(missed)

    if len(missed) == 0:
        print("You completed the quiz in %d rounds!\n" % round_number)

    return round(round_number + 1, missed, translations)


def quiz(wordlist,size):
    n_words = wordlist.get_n_words()
    words = wordlist.words.copy()
    translations = wordlist.translations.copy()
    size = min(size,n_words)

    rand.shuffle(words)
    words = words[:size]

    round(1, words, translations)
