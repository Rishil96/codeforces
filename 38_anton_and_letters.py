# Anton and Letters
# https://codeforces.com/problemset/problem/443/A

def main():
    set_input = input()
    unique = []
    for char in set_input[1:-1].split(", "):
        if char not in unique and char.isalpha():
            unique.append(char)

    print(len(unique))


if __name__ == "__main__":
    main()
