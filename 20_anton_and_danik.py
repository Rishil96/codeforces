# Anton and Danik
# https://codeforces.com/problemset/problem/734/A

def main():
    number_of_games = int(input())
    game_results = input()

    winner = 0

    for i in range(number_of_games):
        if game_results[i] == "A":
            winner += 1
        elif game_results[i] == "D":
            winner -= 1

    if winner > 0:
        print("Anton")
    elif winner < 0:
        print("Danik")
    else:
        print("Friendship")


if __name__ == "__main__":
    main()
