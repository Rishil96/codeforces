# Beautiful Matrix
# https://codeforces.com/problemset/problem/263/A

def main():
    matrix = []
    steps = 0

    for _ in range(5):
        row = input()
        matrix.append(row.split())

    x, y = 0, 0

    for i in range(5):

        if "1" in matrix[i]:
            x = i
            for j in range(5):
                if matrix[i][j] == "1":
                    y = j
                    break
            break

    steps += abs(x - 2)
    steps += abs(y - 2)

    print(steps)


if __name__ == "__main__":
    main()
