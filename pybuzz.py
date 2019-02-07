def pybuzz(n):
    if divisible_by_x(n, 15):
        return 'FizzBuzz'
    elif divisible_by_x(n, 3):
        return 'Fizz'
    elif divisible_by_x(n, 5):
        return 'Buzz'
    return str(n)


def divisible_by_x(n, x):
    if n%x == 0:
        return True
    return False
