from random import randint

randint(1, 100)

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

quantity = input('Введите желаемое количество паролей для генерации?')
length = input('Укажите длину одного пароля?')
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

print(chars)



'''
Количество паролей для генерации;
Длину одного пароля;
Включать ли цифры 0123456789?
Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
Включать ли символы !#$%&*+-=?@^_?
Исключать ли неоднозначные символы il1Lo0O?
'''


