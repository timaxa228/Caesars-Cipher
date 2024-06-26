shifr = input('Шифровать или дешифровать? \n').lower()
while shifr != 'шифр' and shifr != 'дешифр':
    shifr = input('Шифровать или дешифровать? \n').lower()

lang = input('En или Ru? \n').lower()
while lang != 'en' and lang != 'ru':
    lang = input('En или Ru? \n').lower()

shag = input('Шаг сдвига? \n')
while not shag.isdigit():
    shag = input('Шаг сдвига? \n')

en_low_alph = 'abcdefghijklmnopqrstuvwxyz'
ru_low_alph = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

text = input('Введите текст \n')


def cod_decod(shifr, lang, shag, text):
    new_text = ''
    if shifr == 'шифр':
        if lang == 'ru':
            for i in range(len(text)):
                if text[i].isalpha():
                    ind = ru_low_alph.find(text[i].lower())  # индекс буквы из алфавита
                    if text[i].isupper():
                        new_text += ru_low_alph[(ind + int(shag)) % 32].upper()
                    else:
                        new_text += ru_low_alph[(ind + int(shag)) % 32]
                else:
                    new_text += text[i]
        else:   # en
            for i in range(len(text)):
                if text[i].isalpha():
                    ind = en_low_alph.find(text[i].lower())  # индекс буквы из алфавита
                    if text[i].isupper():
                        new_text += en_low_alph[(ind + int(shag)) % 26].upper()
                    else:
                        new_text += en_low_alph[(ind + int(shag)) % 26]
                else:
                    new_text += text[i]
    else:   # дешифр
        if lang == 'ru':
            for i in range(len(text)):
                if text[i].isalpha():
                    ind = ru_low_alph.find(text[i].lower())  # индекс буквы из алфавита
                    if text[i].isupper():
                        new_text += ru_low_alph[(ind - int(shag)) % 32].upper()
                    else:
                        new_text += ru_low_alph[(ind - int(shag)) % 32]
                else:
                    new_text += text[i]
        else:   # en
            for i in range(len(text)):
                if text[i].isalpha():
                    ind = en_low_alph.find(text[i].lower())  # индекс буквы из алфавита
                    if text[i].isupper():
                        new_text += en_low_alph[(ind - int(shag)) % 26].upper()
                    else:
                        new_text += en_low_alph[(ind - int(shag)) % 26]
                else:
                    new_text += text[i]
    print(new_text)


cod_decod(shifr, lang, shag, text)
