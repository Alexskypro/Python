x = int(input("Введите число: "))


def fizz_buzz(x):
    for y in range(1, x):
        if y % 3 == 0 and y % 5 == 0:
            print('FizzBuzz')
        elif y % 3 == 0:
            print('Fizz')
        elif y % 5 == 0:
            print('Buzz')
        else:
            print(y)


fizz_buzz(x)
