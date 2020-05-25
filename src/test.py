import os
import sys
import random as rand
from googletrans import Translator
from spellchecker import SpellChecker
from filemanager import FileManager
from wordlist import WordList
from quiz import quiz
from interface import interface


def test(name):
    os.system('clear')
    interface()
    # translator = Translator()
    # translation_data = translator.translate('regodeo', dest='en',src='es').extra_data
    # print(translation_data['translation'][0][0])
    # print(translation_data['translation'][0][1])


if __name__ == '__main__':
    test('test')
