# A watermelon
# https://codeforces.com/problemset/problem/4/A

def main():
    watermelon_weight = int(input())
    if watermelon_weight % 2 == 0:
        if watermelon_weight == 2:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
