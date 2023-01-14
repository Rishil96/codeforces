# Stones on the table
# https://codeforces.com/problemset/problem/266/A

def main():
    number_of_stones = int(input())
    stones = input()
    output = 0

    for i in range(number_of_stones - 1):
        if stones[i] == stones[i+1]:
            output += 1

    print(output)


if __name__ == "__main__":
    main()
