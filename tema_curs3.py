# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care
# reprezintă numere întregi sau reale.

# your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
# your_function() va returna 0.
# your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).

def your_function(*args, **kwargs):
    my_sum = 0
    for i in args:
        if type(i) == int:
            my_sum += i
    return my_sum


print(your_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(your_function())
print(your_function(2, 4, 'abc', param_1=2))


# Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
# suma tuturor numerelor de la [0, n]
# suma numerelor pare de la [0, n]
# suma numerelor impare de la [0. n]

sum_all, sum_even, sum_odd = 0, 0, 0


def rec_fn(n):
    global sum_all, sum_even, sum_odd

    if n == 0:
        print(f'suma tuturor numerelor de la [0, {n}]: {sum_all}')
        print(f'suma numerelor pare de la [0, {n}]: {sum_even}')
        print(f'suma numerelor impare de la [0. {n}]: {sum_odd}')

        return 0

    sum_all += n

    if n % 2 == 0:
        sum_even += n

    if n % 2 != 0:
        sum_odd += n

    return rec_fn(n - 1)


rec_fn(7)

# Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg,
# altfel returnează valoarea 0.


def check_input():
    user_input = input()

    try:
        return int(user_input)
    except ValueError:
        return 0


print(check_input())
