"""
    Basic python replace method showcase.
"""


def replace_word():
    sentence = input('Enter the main sentence: ')
    word_to_replace = input('Enter the word to replace: ')
    word_replacement = input('Enter the word replacement: ')
    print(sentence.replace(word_to_replace, word_replacement))


replace_word()
