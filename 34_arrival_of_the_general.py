# Arrival of the General
# https://codeforces.com/problemset/problem/144/A


def main():
    number = int(input())
    squad = [int(m) for m in input().split()]
    seconds = 0
    max_value = max(squad)
    max_index = squad.index(max_value)

    seconds += max_index
    squad.pop(max_index)
    squad = [max_value] + squad

    min_value = min(squad)
    min_index = max(index for index, item in enumerate(squad) if item == min_value)

    seconds += number - min_index - 1
    print(seconds)


if __name__ == "__main__":
    main()
