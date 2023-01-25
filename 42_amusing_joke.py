# Amusing Joke
# https://codeforces.com/problemset/problem/141/A

def main():
    guest = input()
    host = input()
    pile = input()
    l1 = [char for char in guest + host]
    l2 = [char for char in pile]
    l1.sort()
    l2.sort()
    if l1 == l2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
