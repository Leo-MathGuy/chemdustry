from math import nan
from element_data import DATA_PROCESSED


def filter_data(data, col, fil):
    return [
        data["name"][x[0]]
        for x in filter(
            lambda x: fil in x[1] if type(x[1]) == str else False,
            enumerate(data[col]),
        )
    ]


if __name__ == "__main__":
    print("Columns:")
    [print(" -", x) for x in DATA_PROCESSED.columns]

    selection = input("Filter column: ")

    if selection not in DATA_PROCESSED.columns:
        print("Not in cols")
        exit(1)

    filt = input("Filter value: ")

    print(", ".join(filter_data(DATA_PROCESSED, selection, filt)))
