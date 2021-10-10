number = input('Введите число: ')


def check(number):
    try:
        int(number)
        k = 1
        for letter in number:
            if int(letter) % 2 == 0:
                k *= int(letter)
        a = "Произведение четных цифр чила: " + str(k)
    except:
        a = 'Ввели не число!!'
    return a


print(check(number))