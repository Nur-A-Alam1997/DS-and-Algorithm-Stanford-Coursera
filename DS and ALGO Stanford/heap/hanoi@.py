#!/usr/bin/env python3

f=open("hanoi.txt","w")
def tower_of_hanoi(number, beginning, auxiliary, ending):
    if number == 1:
        print(f.write(str("({} -> {})".format(beginning, ending))))

        return

    else:
        tower_of_hanoi(number-1, beginning, ending, auxiliary)
        tower_of_hanoi(1, beginning, auxiliary, ending)
        tower_of_hanoi(number-1, auxiliary, beginning, ending)
        
        
# print(tower_of_hanoi)           



def main():
    n = int(input("Enter the number of pieces: "))
    beg = input("Enter the starting rod: ")
    aux = input("Enter the auxiliary rod: ")
    end = input("Enter the final rod: ")

    tower_of_hanoi(n, beg, aux, end)
    
    
    


if __name__ == '__main__':
    main()
    
# f.write(str(tower_of_hanoi(5, 1, 2, 3)))    

f.close()