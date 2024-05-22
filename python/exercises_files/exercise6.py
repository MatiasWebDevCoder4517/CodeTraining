#### look at the exercise6.png image in folder exercises_images


## Solution 1
def stableInternships(interns, teams):
    chosen_interns = {}
    free_interns = list(range(len(interns)))
    current_intern_choices = [0] * len(interns)

    team_maps = []
    for team in teams:
        rank = {}
        for index, intern_num in enumerate(team):
            rank[intern_num] = index
        team_maps.append(rank)

    while len(free_interns) > 0:
        intern_num = free_interns.pop()
        intern = interns[intern_num]
        team_preference = intern[current_intern_choices[intern_num]]
        current_intern_choices[intern_num] += 1

        if team_preference not in chosen_interns:
            chosen_interns[team_preference] = intern_num
            continue

        previous_intern = chosen_interns[team_preference]
        previous_intern_rank = team_maps[team_preference][previous_intern]
        current_intern_rank = team_maps[team_preference][intern_num]

        if current_intern_rank < previous_intern_rank:
            free_interns.append(previous_intern)
            chosen_interns[team_preference] = intern_num
        else:
            free_interns.append(intern_num)
    matches = [
        [intern_num, team_num] for team_num, intern_num in chosen_interns.items()
    ]
    return matches


interns = [[0, 1, 2], [1, 2, 0], [2, 0, 1]]
teams = [[2, 1, 0], [1, 2, 0], [0, 2, 1]]
print(stableInternships(interns, teams))