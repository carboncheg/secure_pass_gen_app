import data
from random import randint

while True:
    num_pass = input('Введите количество паролей: ')
    if not num_pass.isdigit() or int(num_pass) < 1:
        continue
    else:
        break

for i in range(int(num_pass)):
    while True:
        len_pass = input('Укажите длину пароля: ')
        if not len_pass.isdigit() or int(len_pass) < 1:
            continue
        else:
            break

    chars = ''

    def generate_password(len_pass, chars):

        while True:
            is_include_nums = input('Включать цифры? (да - "+", нет - "-") ')
            if is_include_nums == '+':
                chars += data.digits
                break
            elif is_include_nums == '-':
                break
            else:
                continue

        while True:
            is_include_low_let = input('Включать строчные буквы? (да - "+", нет - "-") ')
            if is_include_low_let == '+':
                chars += data.lowercase_letters
                break
            elif is_include_low_let == '-':
                break
            else:
                continue

        while True:
            is_include_upp_let = input('Включать заглавные буквы? (да - "+", нет - "-") ')
            if is_include_upp_let == '+':
                chars += data.uppercase_letters
                break
            elif is_include_upp_let == '-':
                break
            else:
                continue

        while True:
            is_include_symb = input('Включать символы? (да - "+", нет - "-") ')
            if is_include_symb == '+':
                chars += data.symbols
                break
            elif is_include_symb == '-':
                break
            else:
                continue

        while True:
            is_exclude_ambig_chars = input('Исключать неоднозначные символы: "l,I,0,O"? (да - "+", нет - "-") ')
            chars_ambigless = ''
            if is_exclude_ambig_chars == '+':
                for c in chars:
                    if c not in data.ambiguous_characters:
                        chars_ambigless += c
                chars = chars_ambigless
                break
            elif is_exclude_ambig_chars == '-':
                break
            else:
                continue

        i = 0
        password = ''
        while i < int(len_pass):
            gen_char = randint(0, len(chars) - 1)
            password += str(chars[gen_char])
            i += 1

        return password

    pswd = generate_password(len_pass, chars)
    print(pswd)

    if len(pswd) < 9:
        print('Это слабый пароль')
    elif len(pswd) > 9:
        counter = 0
        for c in data.digits:
            if c in pswd:
                counter += 1
                break
        for c in data.lowercase_letters:
            if c in pswd:
                counter += 1
                break
        for c in data.uppercase_letters:
            if c in pswd:
                counter += 1
                break
        for c in data.symbols:
            if c in pswd:
                counter += 1
                break
        if counter == 4:
            print('Это сильный пароль')
