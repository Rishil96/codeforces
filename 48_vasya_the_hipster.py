# Vasya the Hipster
# https://codeforces.com/problemset/problem/581/A

def main():
    red, blue = input().split()
    red, blue = int(red), int(blue)

    days_with_different_pairs = red if red < blue else blue

    days_with_same_pairs = (red-blue)//2 if red > blue else (blue-red)//2

    print(days_with_different_pairs, days_with_same_pairs)


if __name__ == "__main__":
    main()
