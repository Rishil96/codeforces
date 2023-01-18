# Magnets
# https://codeforces.com/problemset/problem/344/A

def main():
    magnets = []
    pairs = 1
    no_of_magnets = int(input())

    for m in range(no_of_magnets):
        magnets.append(input())

    for i in range(no_of_magnets - 1):
        if magnets[i][-1] == magnets[i+1][0]:
            pairs += 1

    print(pairs)


if __name__ == "__main__":
    main()
