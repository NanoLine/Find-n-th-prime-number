def isPrime(a: int):
    if a <= 1 or a % 2 == 0:
        return False
    if a == 2:
        return True
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True

def f(a: int):
    arr: list = [2, 3, 5, 7]
    if len(arr) >= a:
        return arr[a-1]
    i = 11
    while True:
        if isPrime(i):
            arr.append(i)
        if len(arr) >= a:
            return arr[a-1]
        i += 2
