# Insomnia Cure
# https://codeforces.com/problemset/problem/148/A

def main():
    k_input = int(input())  # Punched by frying pan.
    l_input = int(input())  # Tail shut into the balcony door.
    m_input = int(input())  # Paws trampled with sharp heels.
    n_input = int(input())  # Mom called and withdrew.
    d_input = int(input())  # Number of dragons

    slayed = 0
    for dragon in range(1, d_input + 1):
        if dragon % k_input == 0 or dragon % l_input == 0 or dragon % m_input == 0 or dragon % n_input == 0:
            slayed += 1
        else:
            continue
    print(slayed)


if __name__ == "__main__":
    main()
