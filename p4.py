# Задача 4* (Дополнительная). Реализуйте игру «Поле чудес». 
# Вопрос и правильный ответ сохраните в файл. 
# Реализуйте алгоритм шифрования правильного ответа.
from cryptography.fernet import Fernet
from random import randint

secret = ''

def Decrypt_code():
    global secret

    with open('text.txt', 'r', encoding='utf-8') as file:
        s = file.read()
    s = s.split('\n')

    while (True):
        rr = randint(0, 9)
        if rr != 0 and rr % 2 != 0:
            rr = randint(0, 9)
        else:
            break
    if rr == 0:
        secret = 'Он не злой, наоборот,Добродушный, милый...'
        decMessage = Fernet(s[1].encode('utf-8')).decrypt(s[0].encode('utf-8')).decode()
    elif rr == 2:
        secret = 'Кто ходит сидя?'
        decMessage = Fernet(s[3].encode('utf-8')).decrypt(s[2].encode('utf-8')).decode()
    elif rr == 4:
        secret = 'Ежедневно в шесть утра,Я трещу: вставать пора!'
        decMessage = Fernet(s[5].encode('utf-8')).decrypt(s[4].encode('utf-8')).decode()
    elif rr == 6:
        secret = 'Какое слово в словаре написано неправильно?'
        decMessage = Fernet(s[7].encode('utf-8')).decrypt(s[6].encode('utf-8')).decode()
    elif rr == 8:
        secret = 'Речка спятила с ума По домам пошла сама.'
        decMessage = Fernet(s[9].encode('utf-8')).decrypt(s[8].encode('utf-8')).decode()
    return decMessage

def Hidden_word(s):
    hidden_word = str(s).strip("[]").replace("'", '').replace(', ', ' ')
    return hidden_word

word = Decrypt_code()
s = ['\u00B7'] * len(word)
len_word = len(word)
count = 1

print(f'\nДоступно {len_word} попыток\nСлово состоит из ({len(word)}) букв')

while (True):
    print(f'==============================\nЗагадка: {secret}\n\t{Hidden_word(s)}')

    if count > len_word:
        print("Вы проиграли")
        break
    if not '\u00B7' in Hidden_word(s):
        print(f'\t{Hidden_word(s)}')
        print("Победа!!")
        break
    
    print(f'\nПопытка {count}')
    letter = input("Введите букву или слово: ").lower()

    if word.count(letter) and len(letter) == len(word):
        for i in range(0, len(word)):
                s[i] = letter[i]
        print(f'\t{Hidden_word(s)}\nПобеда!!!')
        break

    for i in range(0, len(word)):
        if letter == word[i]:
            s[i] = letter
    print(f'==============================\n')
    count += 1

# ================================
def Encrypting_code():
    f = ''
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encMessage = fernet.encrypt(f.encode())

    key = str(key).split("'")[1]
    encMessage = str(encMessage).split("'")[1]

    with open('text.txt', 'a', encoding='utf-8') as file:
        file.write(encMessage + '\n')
        file.write(key)

# Encrypting_code()



