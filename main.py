from random import randint
import itertools


def pi():
    pi = str(3.141592653589793)

    num = input('Введите: ')

    d = (len(num))

    print(str(pi[:d]))


def find_mult(num):
    multipliers = []
    div = 2
    while num > 1:
        while num % div == 0:
            multipliers.append(div)
            num //= div
        div += 1
    return multipliers

a, b = 15, 45
multipliers_a = find_mult(a)
multipliers_b = find_mult(b)


print(multipliers_a, multipliers_b)
res = 1
for i in set(multipliers_b).intersection(set(multipliers_a)):
    res *= i
print('НОК', res)
print(round(a * b / res))


numbers = [1, 1, 58, 20, 11, 35, 44, 44]
def unique_num(numbers):

    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique

print(unique_num(numbers))




k = randint(2, 7)


def get_ratios(k):
    ratios = [randint(0, 10) for i in range(k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10)
    return ratios


def get_polynomial(k, ratios):
    var = ['*x^'] * (k - 1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')


ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(polynom1)

with open('33_Polynomial.txt', 'w') as data:
    data.write(polynom1)

# Второй многочлен для следующей задачи:

k = randint(2, 5)

ratios = get_ratios(k)
polynom2 = get_polynomial(k, ratios)
print(polynom2)

with open('33_Polynomial2.txt', 'w') as data:
    data.write(polynom2)



while True:

    ex_number = input("\033[34mВведите номер задачи от 1 до 3. Для выхода нажмите 0. \033[0m")
    if ex_number == "1":
        pi()
    elif ex_number == "2":
        find_mult()
    elif ex_number == "3":
        unique_num()
    # elif ex_number == "4":
    #     get_ratios()
    elif ex_number == "0":
        exit()
    print()
