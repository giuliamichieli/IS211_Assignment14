def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def compareTo(s1, s2):
    if s1 < s2:
        return -1
    elif s1 == s2:
        return 0
    elif s1 > s2:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])
    

def main ():
    print("The 10th element of the fibonacci sequence is {}.".format(fibonacci(10)))
    print("The GCD of 16 and 48 is {}.".format(gcd(32, 96)))
    print("Comparison string1 and string2 results in {}.".format(compareTo("whats for string1", "whats for ststringr2")))


if __name__ == '__main__':
    main()
