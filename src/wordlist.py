import os
import sys
import random as rand
from googletrans import Translator
from spellchecker import SpellChecker
from filemanager import FileManager


class WordList:
    def __init__(self,name):
        self.name = name
        self.fm = FileManager(name)
        self.translator = Translator()
        self.words, self.translations, self.n_words = self.fm.read_in()

    @property

    def get_words(self):
        return self.words

    def get_translations(self):
        return self.translations

    def get_name(self):
        return self.name

    def get_n_words(self):
        return self.n_words

    def word_in_list(self, word):
        return True if word in self.words else False

    def add_word(self,word,translations):

        if self.word_in_list(word):
            return None

        # translation_data = self.translator.translate(word, dest='en',src='es').extra_data
        #
        # if not is_word(translation_data):
        #     return get_possible_mistakes(translation_data)
        #
        # translations = get_translations(translation_data)

        self.words.append(word)
        self.translations.update( {word : translations} )
        self.n_words += 1

        self.fm.write_word(word,translations)

    def delete_word(self,word):

        if word not in self.words:
            return None

        self.words.remove(word)
        del self.translations[word]
        self.n_words -= 1

        self.fm.erase_word(word)

    def clear_words(self):
        words = []
        translations = {}
        self.fm.clear_words()


def get_translations(translation_data):
    translations = []
    translations.append(translation_data['translation'][0][0].lower())

    for wc in translation_data['all-translations']:
        for t in wc[1]:
            if t != translations[0]: translations.append(t)

    return translations

def is_word(translation_data):
    if translation_data['all-translations'] == None:
        return False
    else:
        return True

def get_possible_mistakes(translation_data):
    pm = translation_data['possible-mistakes']
    return pm[1] if pm != None else None
