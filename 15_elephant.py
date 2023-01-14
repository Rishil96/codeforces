# Elephant
# https://codeforces.com/problemset/problem/617/A

def main():
    location = int(input())
    steps = location // 5
    if location % 5 != 0:
        steps += 1
    print(steps)


if __name__ == "__main__":
    main()
