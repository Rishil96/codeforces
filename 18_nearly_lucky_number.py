# Nearly lucky number
# https://codeforces.com/problemset/problem/110/A

def main():
    num = int(input())
    lucky_count = 0
    while num != 0:
        if num % 10 in [4, 7]:
            lucky_count += 1
        num //= 10

    if lucky_count in [4, 7]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
