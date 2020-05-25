from googletrans import Translator
import os

'''
    0: 'translation',
    1: 'all-translations',
    2: 'original-language',
    5: 'possible-translations',
    6: 'confidence',
    7: 'possible-mistakes',
    8: 'language',
    11: 'synonyms',
    12: 'definitions',
    13: 'examples',
    14: 'see-also',
'''

os.system('clear')

translator = Translator()

word = 'inmutarse'


trans = translator.translate(word, dest='en',src='es').extra_data

print(translator.translate(word, dest='en',src='es'))

print(trans['translation'][0])
print(trans['all-translations'][0])

for wc in trans['all-translations']:
    for t in wc[1]:
        print(t)
# print(trans['original-language'])
print(trans['possible-translations'])
print(trans['confidence'])
#print(trans['possible-mistakes'])
# print(trans['language'])
# print(trans['synonyms'])
# print(trans['definitions'])
# print(trans['examples'])
# print(trans['see-also'])
