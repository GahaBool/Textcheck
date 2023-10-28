from spellchecker import SpellChecker

def CheckText(text):

    spell = SpellChecker(language="ru")

    mistakes = spell.unknown(text.split())

    for mistake in mistakes:
        print("Исправленный текст: ", spell.correction(mistake))

text = input("Введите текст: ")
CheckText(text)