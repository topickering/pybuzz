def pybuzz(n):
    if n%3 == 0:
        return 'Fizz'
    elif n%5 == 0:
        return 'Buzz'
    return str(n)
