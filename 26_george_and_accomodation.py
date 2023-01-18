# George and Accommodation
# https://codeforces.com/problemset/problem/467/A

def main():
    rooms = int(input())
    available = 0
    for room in range(rooms):
        p, q = input().split()
        p, q = int(p), int(q)
        if q - p > 1:
            available += 1
    print(available)


if __name__ == "__main__":
    main()
