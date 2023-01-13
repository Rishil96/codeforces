# Domino Piling
# https://codeforces.com/problemset/problem/50/A

def main():

    dimensions = input()
    length, width = dimensions.split()
    length = int(length)
    width = int(width)

    l1, l2 = length//2, length % 2
    placed_dominos = l1 * width
    if l2 == 1:
        placed_dominos += width//2

    print(placed_dominos)


if __name__ == "__main__":
    main()
