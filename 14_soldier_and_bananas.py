# Soldier and Bananas
# https://codeforces.com/problemset/problem/546/A

def main():
    user_input = input()
    banana_price, balance, to_buy = user_input.split()
    banana_price, balance, to_buy = int(banana_price), int(balance), int(to_buy)
    total = 0
    for i in range(1, to_buy+1):
        total += banana_price * i
    if total <= balance:
        print(0)
    else:
        print(total - balance)


if __name__ == "__main__":
    main()
