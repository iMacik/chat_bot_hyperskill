def greet(bot_name, birth_year):
    print('Здраствуй! Мое имя ' + bot_name + '.')
    print('Я был создан ' + birth_year + '.')


def remind_name():
    print('Пожалуйста, напомните мне ваше имя.')
    name = input()
    print('Какое у тебя замечательное имя, ' + name + '!')


def guess_age():
    print('Позвольте мне угадать ваш возраст.')
    print('Введите остатки от деления вашего возраста на 3, 5 и 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Ваш возраст " + str(age) + "; это хорошее время, чтобы начать программировать!")


def count():
    print('Сейчас я докажу вам, что могу считать до любого числа, которое вы хотите.')
    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def oprosnik():
    print("Давайте проверим ваши знания в области программирования.")
    print('Почему мы используем методы?')
    print('1. Повторить утверждение несколько раз.')
    print('2. Разложить программу на несколько небольших подпрограмм.')
    print('3. Чтобы определить время выполнения программы.')
    print('4. Прервать выполнение программы.')
    while True:
        answer = int(input())
        corect = 2
        if answer == corect:
            break
        else:
            print('Пожалуйста, попробуйте еще раз.')


def end():
    print('Поздравляю, хорошего дня!')


greet('Gachi' , '2022')
remind_name()
guess_age()
count()
oprosnik()
end()
