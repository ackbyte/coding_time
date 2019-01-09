from glob import glob
from pprint import pprint
import os

stats = {}

users = glob("./course_1/users/*")

for user in users:
    stats.setdefault('0', [" "])
    stats['0'].append(os.path.basename(user))


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            numb, yesno = line.split("=")
            stats.setdefault(numb, [])
            stats[numb].append(yesno)


read_file("./course_1/themes.txt")

for user in users:
    read_file(user)

lengths = []

# Creating stats

text = ""

for lesson in stats:
    line = " | ".join(stats[lesson])
    text += "\n| {} | {} |".format(lesson, line)


with open("./course_1/stats.txt", "w", encoding="utf-8") as file:
    file.write(text)
