def print_formatted(number):
    space=len(bin(number)[2:])+1
    for i in range(1,number+1):
        print(str(i).rjust(space-1," "),end="")
        print(str(oct(i))[2:].rjust(space," "),end="")
        print(str(hex(i))[2:].rjust(space," ").upper(),end="")
        print(str(bin(i))[2:].rjust(space," "))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
