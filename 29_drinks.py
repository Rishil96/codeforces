# Drinks
# https://codeforces.com/problemset/problem/200/B

def main():
    number_of_drinks = int(input())
    all_drinks = input()
    all_drinks = [int(drink) for drink in all_drinks.split()]

    drink_percentage = (sum(all_drinks) / number_of_drinks)
    print(drink_percentage)


if __name__ == "__main__":
    main()
