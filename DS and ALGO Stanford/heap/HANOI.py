#!/usr/bin/env python3


def tower_of_hanoi(number, beginning, auxiliary, ending):
    if number == 1:
        print("{} -> {}".format(beginning, ending))
        return

    else:
        tower_of_hanoi(number-1, beginning, ending, auxiliary)
        tower_of_hanoi(1, beginning, auxiliary, ending)
        tower_of_hanoi(number-1, auxiliary, beginning, ending)


def main():
    n = int(input("Enter the number of pieces: "))
    beg = input("Enter the starting rod: ")
    aux = input("Enter the auxiliary rod: ")
    end = input("Enter the final rod: ")

    tower_of_hanoi(n, beg, aux, end)


if __name__ == '__main__':
    main()