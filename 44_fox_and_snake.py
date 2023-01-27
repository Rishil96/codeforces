# Fox and Snake
# https://codeforces.com/problemset/problem/510/A

def main():
    row, col = input().split()
    row, col = int(row), int(col)
    turn = -1

    for r in range(row):
        if r % 2 == 0:
            print("#" * col)
        else:
            if turn < 0:
                print("." * (col-1) + "#")
                turn *= -1
            else:
                print("#" + "." * (col-1))
                turn *= -1


if __name__ == "__main__":
    main()
