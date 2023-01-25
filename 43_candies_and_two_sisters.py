# Candies and two sisters
# https://codeforces.com/problemset/problem/1335/A

def main():
    test_cases = int(input())
    for test in range(test_cases):
        candies = int(input())
        if candies % 2 == 0:
            print(candies // 2 - 1)
        else:
            print(candies // 2)


if __name__ == "__main__":
    main()
