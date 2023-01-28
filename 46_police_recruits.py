# Police Recruits
# https://codeforces.com/problemset/problem/427/A

def main():
    number_of_events = int(input())
    all_events = [int(event) for event in input().split()]

    officers = 0
    unattended_crimes = 0

    for event in all_events:
        if event == -1:
            if officers > 0:
                officers -= 1
            else:
                unattended_crimes += 1
        else:
            officers += event

    print(unattended_crimes)


if __name__ == "__main__":
    main()
