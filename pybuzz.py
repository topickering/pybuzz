def pybuzz(n):
    if n%15 == 0:
        return 'FizzBuzz'
    elif n%3 == 0:
        return 'Fizz'
    elif n%5 == 0:
        return 'Buzz'
    return str(n)
