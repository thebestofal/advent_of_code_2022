score = 0
games = []
points = {'X': 1, 'Y': 2, 'Z': 3}

scenarios = {'A': {'X': 3, 'Y': 6, 'Z': 0},
             'B': {'X': 0, 'Y': 3, 'Z': 6},
             'C': {'X': 6, 'Y': 0, 'Z': 3}}

with open('input.txt') as f:
    for line in f:
        games.append((line[0], line[2]))

for game in games:
    score += points[game[1]]
    score += scenarios[game[0]][game[1]]

print(score)
