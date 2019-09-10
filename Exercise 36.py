from bokeh.plotting import figure, show, output_file
import json
from collections import Counter


def load_json(route):
    with open(route, "r") as f:
        birthdays = json.load(f)
    return birthdays


def separa_mes(s):
    a = s.split()
    return a[2]


def paint(c):
    output_file("files/plot.html")
    x_categories =["enero", "febrero", "marzo", "abril", "mayo", "junio",
                   "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    x = list(c.keys())
    y = list(c.values())

    print("Claves:\n")
    print(x)
    print("Valores\n")
    print(y)

    p = figure(x_range=x_categories)
    p.vbar(x=x, top=y, width=0.5)

    show(p)


def main():
    birthdays = load_json("files/birthdays.json")
    dates = birthdays.values()
    months = []
    for i in dates:
        months.append(separa_mes(i))
    c = Counter(months)
    paint(c)


main()
