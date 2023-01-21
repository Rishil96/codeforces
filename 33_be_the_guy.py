# I wanna be the guy
# https://codeforces.com/problemset/problem/469/A

def main():
    cleared = True
    levels = int(input())

    x_ip = input()
    x_ip = [int(i) for i in x_ip.split()]
    x_ip = x_ip[1:]

    y_ip = input()
    y_ip = [int(i) for i in y_ip.split()]
    y_ip = y_ip[1:]

    for level in range(1, levels+1):
        if level in x_ip or level in y_ip:
            continue
        cleared = False
        break

    if cleared:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")


if __name__ == "__main__":
    main()
