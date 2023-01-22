# Divisibility Problem
# https://codeforces.com/problemset/problem/1328/A

def main():
    test_cases = int(input())
    for t in range(test_cases):
        a, b = input().split()
        a, b = int(a), int(b)
        if a % b == 0:
            print(0)
        else:
            value = b * ((a // b) + 1)  # Find the next multiple by adding one to the current quotient of a//b
            print(value - a)


if __name__ == "__main__":
    main()
