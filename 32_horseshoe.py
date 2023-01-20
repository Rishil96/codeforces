# Is your horseshoe on the other hoof?
# https://codeforces.com/problemset/problem/228/A

def main():
    shoes = [shoe for shoe in input().split()]
    print(4 - len(set(shoes)))


if __name__ == "__main__":
    main()
