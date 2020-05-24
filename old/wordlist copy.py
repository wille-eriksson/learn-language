import os
import sys
import random as rand
from googletrans import Translator
from spellchecker import SpellChecker

class WordList:
    def __init__(self,name):
        self.name = name
        self.DELIMITER_1 = "->"
        self.DELIMITER_2 = ","
        self.path = '/Users/willeeriksson/Documents/Programmering/learnspanish/wordlists/%s.txt' % name
        if not os.path.isfile(self.path):
            open(self.path, 'a').close()
        self.translator = Translator()
        self.words = []
        self.translations = {}
        self.n_words = 0
        self.__read_words()

    @property

    def get_words(self):
        return self.words

    def get_translations(self):
        return self.translations

    def get_name(self):
        return self.name

    def add_words(self):

        word = str(input()).lower()

        if word == "!":
            os.system('clear')
            return None
        else:
            self.add_word(word)

        self.add_words()


    def add_word(self,word):

        translation_data = self.translator.translate(word, dest='en',src='es').extra_data
        if not self._check_validity(word, translation_data):
            return None
        translations = self._translate(translation_data)
        self._add_word(word,translations)

        print("The word '%s' was added to the wordlist." % word)
        print("Translation: " + translations[0].capitalize())
        if len(translations) > 1:
            print("Other translations include: " + ", ".join(translations[1:]) + ".")
        print()


    def delete_words(self):


        word = str(input()).lower()

        if word == '!':
            os.system('clear')
            return None

        with open(self.path,'r') as f:
            lines = f.readlines()

        line_to_delete = ""

        for line in lines:
            if line.strip("\n").split("->")[0] == word:
                line_to_delete = line.strip("\n")

        if not line_to_delete:
            print("The word '%s' does not seem to be in the wordlist. \n" % word.capitalize())
            return self.delete_words()

        with open(self.path, "w") as f:
            for line in lines:
                if line.strip("\n") != line_to_delete:
                    f.write(line)
            f.close()
        print("The word '%s' was deleted from the wordlist. \n" % word.capitalize())
        self.words.remove(word)
        del self.translations[word]
        self.n_words -= 1
        return self.delete_words()



    def quiz(self):
        print("How many words do you want for your quiz? The wordlist contains %d words" % self.n_words)
        size = int(input())
        size = min(size,self.n_words)

        os.system('clear')

        words = self.words.copy()

        rand.shuffle(words)
        words = words[:size]

        round = 0

        while words:
            missed = []
            round += 1

            for word in words:
                print("Round %d \n" % round)

                trans = self.translations[word].copy()
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
                input()
                os.system('clear')

            rand.shuffle(missed)
            words = missed
            os.system('clear')

        print("You completed the quiz in %d rounds!\n" % round)


    def clear_words(self):
        print("Are you sure you want to clear all words? (Y/N)")
        ans = str(input()).capitalize()
        if ans == "Y":
            f = open('/Users/willeeriksson/Documents/Programmering/learnspanish/wordlists/spanish.txt', "w")
            f.write("")
            self.words = []
            self.translations = {}
        elif ans == "N":
            pass


    def __read_words(self):

        with open(self.path,'r') as f:
            lines = f.readlines()

        for line in lines:
            word, translations = line.strip("\n").split(self.DELIMITER_1)
            translations = translations.split(self.DELIMITER_2)

            self.words.append(word)
            self.translations.update( {word : translations} )

        self.n_words = len(self.words)

    def _check_validity(self,word,translation_data):
        if self._word_in_list(word):
            print("The word %s is already in the wordlist. \n" % word)
            return False
        elif not self._is_word(translation_data):
            print("The word '%s' does not seem to be in the dictionary." % word)
            pm = self._possible_mistakes(translation_data)
            if pm != None:
                print("Did you mean '%s'?" % pm)
            return False
        else:
            return True


    def _translate(self,translation_data):
        translations = []
        translations.append(translation_data['translation'][0][0].lower())

        for wc in translation_data['all-translations']:
            for t in wc[1]:
                if t != translations[0]: translations.append(t)

        return translations

    def _write_word(self,word,translations):

        translations = self.DELIMITER_2.join(translations)
        to_write = word + self.DELIMITER_1 + translations + "\n"

        f = open(self.path,'a')
        f.write(to_write)
        f.close()

    def _add_word(self, word, translations):

        self.words.append(word)
        self.translations.update( {word : translations} )
        self.n_words += 1

        self._write_word(word,translations)

    def _word_in_list(self, word):
        return True if word in self.words else False

    def _is_word(self,translation_data):
        if translation_data['all-translations'] == None:
            return False
        else:
            return True

    def _possible_mistakes(self,translation_data):
        pm = translation_data['possible-mistakes']
        return pm[1] if pm != None else None
