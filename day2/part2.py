score = 0
games = []
points = {'X': 1, 'Y': 2, 'Z': 3}
points_win_draw_loose = {'X': 0, 'Y': 3, 'Z': 6}

scenarios = {'A': {3: 'X', 6: 'Y', 0: 'Z'},
             'B': {0: 'X', 3: 'Y', 6: 'Z'},
             'C': {6: 'X', 0: 'Y', 3: 'Z'}}


with open('input.txt') as f:
    for line in f:
        games.append((line[0], line[2]))

for game in games:
    score += points_win_draw_loose[game[1]]
    score += points[scenarios[game[0]][points_win_draw_loose[game[1]]]]

print(score)
