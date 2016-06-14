#!/usr/bin/python3


def fizz_buzzify(n):
    return "Fizz" * (n % 3 == 0) + "Buzz" * (n % 5 == 0) or n


def main():
    for i in range(1, 101):
        print(fizz_buzzify(i))


if __name__ == '__main__':
    main()
