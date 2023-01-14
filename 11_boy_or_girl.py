# Boy or Girl
# https://codeforces.com/problemset/problem/236/A

def main():
    name = input()
    if len(set(name)) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")


if __name__ == "__main__":
    main()
