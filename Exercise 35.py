import json
from collections import Counter


def load_json(route):
    with open(route, "r") as f:
        birthdays = json.load(f)
    return birthdays


def separa_mes(s):
    a = s.split()
    return a[2]


def main():
    birthdays = load_json("files/birthdays.json")
    dates = birthdays.values()
    months = []
    for i in dates:
        months.append(separa_mes(i))
    c = Counter(months)
    print(c)


main()
