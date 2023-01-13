# Bit++
# https://codeforces.com/problemset/problem/282/A

def main():
    number_of_instructions = int(input())
    output = 0

    for _ in range(number_of_instructions):
        instruction = input()
        if "++" in instruction:
            output += 1
        elif "--" in instruction:
            output -= 1

    print(output)


if __name__ == "__main__":
    main()
