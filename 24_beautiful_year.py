# Beautiful Year
# https://codeforces.com/problemset/problem/271/A

def main():
    year_input = int(input())
    year = year_input + 1

    while True:
        year_list = [y for y in str(year)]
        if len(set(year_list)) == 4:
            print(year)
            break
        year += 1


if __name__ == "__main__":
    main()
