# Games
# https://codeforces.com/problemset/problem/268/A

def main():
    teams = int(input())
    jerseys = []
    games = 0
    for _ in range(teams):
        home, away = input().split()
        home, away = int(home), int(away)
        jerseys.append([home, away])

    for i in range(len(jerseys)):
        for j in range(i+1, len(jerseys)):
            if jerseys[i][0] == jerseys[j][1]:
                games += 1
            if jerseys[i][1] == jerseys[j][0]:
                games += 1

    print(games)


if __name__ == "__main__":
    main()
