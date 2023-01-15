# Tram
# https://codeforces.com/problemset/problem/116/A

def main():
    stops = int(input())
    current_onboarded = 0
    maximum_capacity = 0

    for _ in range(stops):
        people = input()
        drop, add = people.split()
        drop, add = int(drop), int(add)
        current_onboarded -= drop
        current_onboarded += add
        if current_onboarded > maximum_capacity:
            maximum_capacity = current_onboarded

    print(maximum_capacity)


if __name__ == "__main__":
    main()
