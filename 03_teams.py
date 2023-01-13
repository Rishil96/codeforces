# Teams
# https://codeforces.com/problemset/problem/231/A

def main():
    problems = int(input())
    solutions = 0

    for _ in range(problems):
        answer = input()
        if "1 1" in answer or "1 0 1" in answer:
            solutions += 1

    print(solutions)


if __name__ == "__main__":
    main()
