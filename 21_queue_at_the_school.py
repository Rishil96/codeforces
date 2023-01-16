# Queue at the school
# https://codeforces.com/problemset/problem/266/B

def main():
    first_input = input()
    count, time = first_input.split()
    time = int(time)
    queue = input()

    # queue = [child for child in second_input]

    while time > 0:
        queue = queue.replace("BG", "GB")
        time -= 1

    print(queue)


if __name__ == "__main__":
    main()
