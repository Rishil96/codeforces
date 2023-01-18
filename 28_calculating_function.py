# Calculating Function
# https://codeforces.com/problemset/problem/486/A

def main():
    integer = int(input())

    # O(n)
    # operator = 1
    # answer = 0
    #
    # for i in range(1, integer+1):
    #     operator *= -1
    #     answer += i * operator
    #
    # print(answer)

    # O(1)
    if integer % 2 == 0:
        print(integer // 2)
    else:
        print(-(integer // 2 + 1))


if __name__ == "__main__":
    main()
