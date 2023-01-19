# Ultra-Fast Mathematician
# https://codeforces.com/problemset/problem/61/A

def main():
    num1 = input()
    num2 = input()
    output = ""

    for i in range(len(num1)):
        if num1[i] == num2[i]:
            output += "0"
        else:
            output += "1"

    print(output)


if __name__ == "__main__":
    main()
