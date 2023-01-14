# Bear and Big Brother
# https://codeforces.com/problemset/problem/791/A

def main():
    weights = input()
    lim_weight, bob_weight = weights.split()
    lim_weight, bob_weight = int(lim_weight), int(bob_weight)
    years = 0

    while True:
        if lim_weight > bob_weight:
            break
        lim_weight *= 3
        bob_weight *= 2
        years += 1

    print(years)


if __name__ == "__main__":
    main()
