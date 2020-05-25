import os
import sys
from wordlist import WordList

def list_existing(existing):

    n_exist = len(existing)

    print("(0) Create new" )
    for i in range(0, n_exist):
        print("(%d) " % (i+1) + existing[i].strip('.txt') )

    print("(%d) Exit" % (n_exist+1))

def parse_choice(choice,existing):
    n_exist = len(existing)

    if choice > n_exist+1 or choice < 0:
        print("Not a valid answer.")
        return main()
    elif choice == 0:
        print("Enter the name of your new wordlist")
        name = str(input())
    elif choice == n_exist+1:
        os.system('clear')
        sys.exit()
    else:
        name = existing[choice-1].strip('.txt')
    return name


def choose_wordlist():
    os.system('clear')
    print("What wordlist do you want to use? Choose one:")

    existing = os.listdir('/Users/willeeriksson/Documents/Programmering/learnspanish/wordlists/')

    list_existing(existing)

    choice = int(input())
    name = parse_choice(choice,existing)

    wl = WordList(name)
    return wl

def choose_action(wl):
        os.system('clear')
        print(wl.name + "\n")
        print("What do you want to do? \n Add words : (A) \n Delete words : (D) \n Clear words (C) \n Quiz : (Q) \n Go back : (B)")
        action = str(input()).capitalize()
        os.system('clear')

        if action == "A":
            print("Enter word(s) to add. Enter ! when you are done.")
            wl.add_words()
        elif action == "C":
            wl.clear_words()
        elif action == "D":
            print("Enter word(s) to delete. Enter ! when you are done.")
            wl.delete_words()
        elif action == "Q":
            wl.quiz()
        elif action == "B":
            return main()
        else:
            print("Invalid action")
        return choose_action(wl)

def main():
    wl = choose_wordlist()
    choose_action(wl)

if __name__ == '__main__':
    main()
