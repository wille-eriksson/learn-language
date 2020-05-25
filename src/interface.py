import os
import sys
import random as rand
from wordlist import WordList
from googletrans import Translator


class MainWindow:
    def __init__(self):
        self.names = self.get_existing_wordlists()
        self.n_lists = len(self.names)

    def main(self):
        self.graphic()
        choice = int(input())
        return self.parse_choice(choice)

    def get_existing_wordlists(self):
        path = '/Users/willeeriksson/Documents/Programmering/learnspanish/wordlists'
        existing = os.listdir(path)

        if ".DS_Store" in existing:
            existing.remove(".DS_Store")

        for index, wordlist in enumerate(existing):
            existing[index] = os.path.splitext(wordlist)[0]

        return existing

    def graphic(self):
        os.system('clear')
        print("(0) Create new" )
        for index, wordlist in enumerate(self.names):
            print('(%d) %s' % (index+1, wordlist))

        print("(%d) Exit" % (index+2))

    def parse_choice(self,choice):

        if choice > self.n_lists+1 or choice < 0:
            print("Not a valid answer.")
            return main()
        elif choice == 0:
            print("Enter the name of your new wordlist")
            name = str(input())
        elif choice == self.n_lists+1:
            os.system('clear')
            sys.exit()
        else:
            name = self.names[choice-1]
        return name


class ActionWindow():
    def __init__(self,wordlist):
        self.wordlist = wordlist
        self.name = wordlist.name

    def main(self):
        self.graphic()
        action = str(input()).capitalize()
        self.parse_action(action)

    def parse_action(self,action):
        if action == "A":
            return add_words(self.wordlist)
        elif action == "C":
            return clear_words(self.wordlist)
        elif action == "D":
            return delete_words(self.wordlist)
        elif action == "Q":
            return quiz(self.wordlist)
        elif action == "B":
            return interface()
        else:
            print("Invalid action")
            os.system('clear')
            return self.parse_action()

    def graphic(self):
        os.system('clear')
        print(self.name + "\n")
        print("What do you want to do? \n Add words : (A) \n Delete words : (D) \n Clear words (C) \n Quiz : (Q) \n Go back : (B)")


class AddWindow:
    def __init__(self,wordlist):
        self.wordlist = wordlist
        self.name = wordlist.name

    def main(self):
        self.graphics()
        word = str(input()).lower()

        if word == '!': return choose_action(self.wordlist)

        translations, possible_mistake = get_translations(word)

        if translations == None:
            print("The word '%s' does not seem to be in the dictionary. Did you mean '%s'?\n" % (word, possible_mistake))
            input()
            return self.main()

        self.wordlist.add_word(word, translations)
        print("The word '%s' was added to the wordlist." % word)
        print("Translations include: %s" % ", ".join(translations))
        input()

        return self.main()

    def graphics(self):
        os.system('clear')
        print("Enter word(s) to add. Enter '!' when you are done. There are %d words in this list." % self.wordlist.n_words)

class DeleteWindow:
    def __init__(self,wordlist):
        self.wordlist = wordlist
        self.name = wordlist.name

    def main(self):
        self.graphics()
        word = str(input()).lower()

        if word == '!': return choose_action(self.wordlist)

        if not self.wordlist.word_in_list(word):
            print("The word '%s' does not seem to be in the wordlist." % word)
            input()
            return self.main()

        self.wordlist.delete_word(word)

        return self.main()

    def graphics(self):
        os.system('clear')
        print("Enter word(s) to delete. Enter '!' when you are done.\nWords:")
        for word in self.wordlist.words:
            print(word)


class QuizWindow:
    def __init__(self,wordlist):
        self.wordlist = wordlist
        self.n_words = wordlist.get_n_words()

    def main(self):
        self.graphics()

        size = int(input())

        os.system('clear')

        words = self.wordlist.words.copy()
        translations = self.wordlist.translations.copy()
        size = min(size,self.n_words)

        rand.shuffle(words)
        words = words[:size]

        self.round(1, words, translations)

        return choose_action(self.wordlist)

    def round(self,round_number, words, translations):
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

            if ans == "!":
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

        return self.round(round_number + 1, missed, translations)

    def graphics(self):
        os.system('clear')
        print("How many words do you want in your quiz? There are %d words in the wordlist." % self.n_words)


def add_words(wordlist):
    AW = AddWindow(wordlist)
    return AW.main()

def delete_words(wordlist):
    DW = DeleteWindow(wordlist)
    return DW.main()

def clear_words(wordlist):
    pass

def quiz(wordlist):
    QW = QuizWindow(wordlist)
    return QW.main()

def choose_action(wl):
    AW = ActionWindow(wl)
    return AW.main()



def interface():
    MW = MainWindow()
    wl = WordList(MW.main())
    return choose_action(wl)











def get_translations(word):
    translator = Translator()
    translation_data = translator.translate(word, dest='en',src='es').extra_data

    if not is_word(translation_data):
        return None, get_possible_mistakes(translation_data)

    translations = []
    translations.append(translation_data['translation'][0][0].lower())

    if translation_data['all-translations'] != None:
        for wc in translation_data['all-translations']:
            for t in wc[1]:
                if t != translations[0]: translations.append(t)

    return translations, None

def is_word(translation_data):
    if translation_data['all-translations'] == None and translation_data['translation'][0][0]==translation_data['translation'][0][1]:
        return False
    else:
        return True

def get_possible_mistakes(translation_data):
    pm = translation_data['possible-mistakes']
    return pm[1] if pm != None else None



if __name__ == '__main__':
    interface()
