# Next round
# https://codeforces.com/problemset/problem/158/A

def main():
    passed_students = 0

    first_input = input()

    min_index = first_input.split()[-1]
    min_index = int(min_index)

    scores = input()
    scores = [int(i) for i in scores.split()]
    minimum_passing = scores[min_index - 1]

    for score in scores:
        if score >= minimum_passing and score > 0:
            passed_students += 1

    print(passed_students)


if __name__ == "__main__":
    main()
