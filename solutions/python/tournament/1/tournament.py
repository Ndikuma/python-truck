def tally(matches):
    teams = {}

    def add_team(name):
        if name not in teams:
            teams[name] = {
                "MP": 0,
                "W": 0,
                "D": 0,
                "L": 0,
                "P": 0,
            }

    for line in matches:
        if not line:
            continue

        team1, team2, result = line.split(";")

        add_team(team1)
        add_team(team2)

        teams[team1]["MP"] += 1
        teams[team2]["MP"] += 1

        if result == "win":
            teams[team1]["W"] += 1
            teams[team1]["P"] += 3
            teams[team2]["L"] += 1
        elif result == "loss":
            teams[team2]["W"] += 1
            teams[team2]["P"] += 3
            teams[team1]["L"] += 1
        else:  # draw
            teams[team1]["D"] += 1
            teams[team2]["D"] += 1
            teams[team1]["P"] += 1
            teams[team2]["P"] += 1

    table = ["Team                           | MP |  W |  D |  L |  P"]

    for name, s in sorted(teams.items(), key=lambda x: (-x[1]["P"], x[0])):
        table.append(
            f"{name:<31}| {s['MP']:>2} | {s['W']:>2} | "
            f"{s['D']:>2} | {s['L']:>2} | {s['P']:>2}"
        )

    return table