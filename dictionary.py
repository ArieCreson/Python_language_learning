import json
import random
import subprocess
import sys


def call_script(path, argument):
    # print("test" +argument)
    completed_process = subprocess.run(['bash', path, argument],
                                       text=True,  # Capture output as text
                                       stdout=subprocess.PIPE,  # Capture standard output
                                       stderr=subprocess.PIPE,  # Capture standard error
                                       check=True)  # Raise exception for non-zero exit code

    # Print the captured output
    # print("Script Output:")
    print(completed_process.stdout, end="")
    # print("Script Error (if any):")
    print(completed_process.stderr, end="")


def word_wiktionary(word):
    x = 'https://en.wiktionary.org/wiki/' + word


def prompt(choice):
    if len(choice) > 1:
        word = choice[1]
        # if choice[1]=="last" there might be a problem (see remove functionality)
    else:
        word = input("Enter word: ")
    return word


class WordManager:

    def __init__(self):
        self.words = {}
        self.load_words()

    def save_words(self):
        with open("words.json", "w") as file:
            json.dump(self.words, file)

    def load_words(self):
        try:
            with open("words.json", "r") as file:
                self.words = json.load(file)
        except FileNotFoundError:
            pass

    def add_word(self, word, english_translation):
        word = word.strip()  # Remove leading/trailing spaces
        english_translation = english_translation.strip()  # Remove leading/trailing spaces
        self.words[word] = english_translation
        self.save_words()
        print("The word: \"" + word + "\" has been added!")

    def remove_word(self, word):
        if word in self.words:
            del self.words[word]
            self.save_words()
            print(f"{word} has been removed.")
        else:
            print(f"{word} not found in the dictionary.")

    def get_translation(self, word):
        word = word.strip()
        return self.words.get(word, "Translation not found")

    def shuffle_words(self):
        with open("words.json", "r") as file:
            temp = json.load(file)
        keys = list(temp)
        random.shuffle(keys)
        shuffled = dict()
        for key in keys:
            shuffled.update({key: temp[key]})
        with open("words.json", "w") as file:
            json.dump(shuffled, file)

    def get_random(self):
        with open("words.json", "r") as file:
            temp = json.load(file)
        word = random.choice(list(temp))
        print(word, end='')
        if len(sys.argv) > 1:
            print('')
        else:
            try1 = input(". what's the translation?")
            word = temp[word]
            if try1 in word:
                print("gut gemacht!")
            else:
                print("wrong :(")

    def count_words(self):
        with open("words.json", "r") as file:
            temp = json.load(file)
        print(f"The amount of saved words: {len(temp)}")

    def check_word(self, word):
        with open("words.json", "r") as file:
            temp = json.load(file)
        keys = list(temp)
        if word in keys:
            print(word + " is indeed in the list")
        else:
            print(word + " is not in the list")

    def ai_translate(self, word):
        argument = 'erkläre mir mal, was meint dieses wort:' + word + 'auf Deutsch, einfach und kurz bitte, ' \
                                                                            'besser mit punkte.'
        call_script("ai.sh", argument)

    def ai_call(self, word):
        argument = 'Write a short and precise answer, preferable in points: ' + word
        call_script("ai.sh", word)

    def list_words(self):
        return list(self.words.keys())


def main():
    Program_arg = sys.argv[1:]
    Program_arg = ' '.join(Program_arg)
    word_manager = WordManager()
    last_word = ""
    num_args = len(sys.argv)
    if num_args == 1:
        print("Available commands:")
        print("add, to add a word (example : add Hallo: hello) ")
        print("get, to get translation")
        print("list, to list words")
        print("remove, to remove a word: (example : remove last)")
        print("shuffle, to shuffle the list of words")
        print("count, to display the amount of saved words")
        print("check, to check for the existence of a word")
        print("translate, to translate a word using an advanced AI (arie's api)")
        print("ai, to conversate with an advance AI (arie's api)")
        print("exit, to exit")
    while True:
        choice = ""
        if num_args > 1:
            choice = Program_arg
        while choice == "":
            choice = input("Enter your choice: ")
        choice = choice.split(maxsplit=1)
        if choice[0] == "add":
            word = prompt(choice)
            if len(choice) > 1 and ':' in choice[1]:
                x = choice[1].split(':', maxsplit=1)
                word_manager.add_word(x[0], x[1])
                word = x[0]
            else:
                english_translation = input("Enter translation: ")
                word_manager.add_word(word, english_translation)
            last_word = word
        elif choice[0] == "get":
            word = prompt(choice)
            translation = word_manager.get_translation(word)
            print(f"Translation: {translation}")
        elif choice[0] == "list":
            words = word_manager.list_words()
            if words:
                print("Words in the dictionary:")
                for word in words:
                    print(word)
            else:
                print("No words in the dictionary.")
        elif choice[0] == "remove":

            word = prompt(choice)
            if word == 'last':
                word = last_word
            word_manager.remove_word(word)
            # print(word+" removed successfully!")

        elif choice[0] == "shuffle":
            word_manager.shuffle_words()
            print("Shuffle performed successfully!")
        elif choice[0] == "count":
            word_manager.count_words()
        elif choice[0] == "translate":

            word = prompt(choice)
            word_manager.ai_translate(word)

        elif choice[0] == "check":
            word = prompt(choice)
            word_manager.check_word(word)

        elif choice[0] == "ai":
            word = prompt(choice)
            word_manager.ai_call(word)


        elif choice[0] == "wikt":
            word = prompt(choice)

            print("Exiting the program.")
            break

        elif choice[0] == "exit":
            word_manager.save_words()  # Save words before exiting
            print("Exiting the program.")
            break
        elif choice[0] == "random":
            word_manager.get_random()  # Save words before exiting



        else:
            print("Invalid choice. Please choose a valid option.")
        if num_args > 1:
            break


if __name__ == "__main__":
    main()
