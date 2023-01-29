# Sum of Round Numbers
# https://codeforces.com/problemset/problem/1352/A

def main():

    tests = int(input())

    for _ in range(tests):
        number = int(input())
        round_nums = []
        divisor = 10
        while True:
            if divisor > number:
                break
            if number % divisor == 0:
                divisor *= 10
            else:
                round_nums.append(number % divisor)
                number -= number % divisor

        round_nums.append(number)
        print(len(round_nums))
        print(*round_nums)


if __name__ == "__main__":
    main()
