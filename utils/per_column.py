from element_data import DATA_PROCESSED


def getCols(data, column):
    if column not in data.columns:
        print("Not in cols")

    if column == "name":
        print(", ".join(data["name"].values))
    else:
        returned = []
        for i in data["name"].values:
            returned.append([i, data.loc[data["name"] == i, column].to_numpy()[0]])

        return returned


if __name__ == "__main__":
    print("Columns:")
    [print(" -", x) for x in DATA_PROCESSED.columns]

    selection = input("Column 2: ")

    print(getCols(DATA_PROCESSED, selection))
