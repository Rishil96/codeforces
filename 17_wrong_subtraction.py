# Wrong Subtraction
# https://codeforces.com/problemset/problem/977/A

def main():
    numbers = input()
    n1, n2 = numbers.split()
    n1, n2 = int(n1), int(n2)

    for i in range(n2):
        if n1 % 10 == 0:
            n1 //= 10
        else:
            n1 -= 1

    print(n1)


if __name__ == "__main__":
    main()
