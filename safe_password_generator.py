import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

quantity = int(input('Введите желаемое количество паролей для генерации?'))
length = int(input('Укажите длину одного пароля?'))
num_ok = input('Включать ли цифры? да/нет')
char_up = input('Включать ли прописные буквы? да/нет')
char_low = input('Включать ли строчные буквы? да/нет')
symbol = input('Включать ли символы? да/нет')
similar_sym = input('Исключать ли неоднозначные символы? да/нет')

if num_ok.lower() == 'да':
    chars += digits
if char_up.lower() == 'да':
    chars += uppercase_letters
if char_low.lower() == 'да':
    chars += lowercase_letters
if symbol.lower() == 'да':
    chars += punctuation
if similar_sym.lower() == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password


for _ in range(quantity):
    print(generate_password(length, chars))
