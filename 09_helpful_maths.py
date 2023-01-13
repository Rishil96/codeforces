# Helpful Maths
# https://codeforces.com/problemset/problem/339/A

def main():
    expression = input()
    operands = [i for i in expression.split("+")]
    operands.sort()
    print("+".join(operands))


if __name__ == "__main__":
    main()
