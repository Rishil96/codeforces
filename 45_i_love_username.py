# I love username
# https://codeforces.com/problemset/problem/155/A

def main():
    number = int(input())
    points = [int(pt) for pt in input().split()]
    amazing = 0

    for i in range(1, len(points)):
        if points[i] > max(points[:i]) or points[i] < min(points[:i]):
            amazing += 1

    print(amazing)


if __name__ == "__main__":
    main()
