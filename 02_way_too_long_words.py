# Way too long words
# https://codeforces.com/problemset/problem/71/A

def main():
    number = int(input())
    for i in range(number):
        word = input()
        if len(word) <= 10:
            print(word)
        else:
            print(f"{word[0]}{len(word) - 2}{word[-1]}")


if __name__ == "__main__":
    main()
