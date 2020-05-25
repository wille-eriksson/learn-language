import os
import sys

class FileManager:
    DELIMITER_1 = "->"
    DELIMITER_2 = ","

    def __init__(self,name):
        self.path = '/Users/willeeriksson/Documents/Programmering/learnspanish/wordlists/%s.txt' % name
        if not os.path.isfile(self.path):
            open(self.path, 'a').close()

    def read_in(self):

        words = []
        translations = {}

        with open(self.path,'r') as f:
            lines = f.readlines()

        for line in lines:
            word, translation = line.strip("\n").split(self.DELIMITER_1)
            translation = translation.split(self.DELIMITER_2)

            words.append(word)
            translations.update( {word : translation} )

        n_words = len(words)

        return words, translations, n_words

    def write_word(self,word,translations):

        translations = self.DELIMITER_2.join(translations)
        to_write = word + self.DELIMITER_1 + translations + "\n"

        f = open(self.path,'a')
        f.write(to_write)
        f.close()

    def erase_word(self,word):

        with open(self.path,'r') as f:
            lines = f.readlines()

        with open(self.path, "w") as f:
            for line in lines:
                if line.strip("\n").split(self.DELIMITER_1)[0] != word:
                    f.write(line)

        f.close()

    def clear_words(self):
            f = open(self.path, "w").close()
