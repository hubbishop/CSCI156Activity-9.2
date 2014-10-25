__author__ = 'Dark-Knight'


def capitalcase():
    with open("r.txt", "rt", encoding="utf-8")as f:
        for line in f:
            line.upper()
            print(line.upper())
capitalcase()
