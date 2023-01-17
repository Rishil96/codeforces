# Vanya and Fence
# https://codeforces.com/problemset/problem/677/A

def main():
    n, h = input().split()
    h = int(h)
    width = 0

    # height = input()
    heights = [int(height) for height in input().split()]
    for height in heights:
        if height > h:
            width += 2
        else:
            width += 1

    print(width)


if __name__ == "__main__":
    main()
