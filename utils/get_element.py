from curses.ascii import isdigit
from element_data import DATA_PROCESSED

name = input("Name or number of element: ")

id = None
if name.isdigit():
    id = int(name)

if not id:
    id = DATA_PROCESSED.loc[DATA_PROCESSED["name"] == name]["number"].to_numpy()[0] - 1

for column in DATA_PROCESSED.columns:
    print(column, "-", DATA_PROCESSED.loc[id, column])
