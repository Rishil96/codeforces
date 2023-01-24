# Hit the Lottery
# https://codeforces.com/problemset/problem/996/A

def main():
    balance = int(input())
    notes = 0
    denominations = [100, 20, 10]
    notes += balance // 100
    balance %= 100

    notes += balance // 20
    balance %= 20

    notes += balance // 10
    balance %= 10

    notes += balance // 5
    balance %= 5

    notes += balance

    print(notes)


if __name__ == "__main__":
    main()
