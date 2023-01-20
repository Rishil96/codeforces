# Hulk
# https://codeforces.com/problemset/problem/705/A

def main():
    hate = "I hate "
    love = "I love "
    it = "it "
    that = "that "
    output = ""
    layers = int(input())

    for i in range(1, layers+1):
        if i == layers:
            if i % 2 != 0:
                output += hate + it
            else:
                output += love + it
        else:
            if i % 2 != 0:
                output += hate + that
            else:
                output += love + that
    print(output.strip())


if __name__ == "__main__":
    main()
