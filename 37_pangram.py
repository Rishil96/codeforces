# Pangram
# https://codeforces.com/problemset/problem/520/A

def main():
    is_pan = True
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    number = int(input())
    phrase = input().lower()
    for alphabet in alphabets:
        if alphabet not in phrase:
            is_pan = False
            break

    if is_pan:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
