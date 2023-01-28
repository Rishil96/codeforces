# New Year and Hurry
# https://codeforces.com/problemset/problem/750/A

def main():
    problems, minutes = input().split()
    problems, minutes = int(problems), int(minutes)
    problems_solved = 0
    time_used = 0

    for problem in range(1, problems+1):
        time_used += 5 * problem
        if time_used + minutes > 240:
            break
        else:
            problems_solved += 1

    print(problems_solved)


if __name__ == "__main__":
    main()
