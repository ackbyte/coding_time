stats = {}

with open("themes.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        numb, yesno = line.split("=")
        stats.setdefault(numb, [])
        stats[numb].append(yesno)

with open("users/Shadow2302", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        numb, yesno = line.split("=")
        stats.setdefault(numb, [])
        stats[numb].append(yesno)

with open("users/tromboid", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        numb, yesno = line.split("=")
        stats.setdefault(numb, [])
        stats[numb].append(yesno)

print(stats)
