from io import StringIO
from urllib import request
import pandas as pd


DATA_URL = "https://github.com/dedolist/open-data/raw/master/data/science/periodic-table-detailed/data.csv"

print("Sending request...")
PER_DATA: str = request.urlopen(DATA_URL).read()
print("Recieved\n")
DATA_PROCESSED: pd.DataFrame = pd.read_csv(StringIO(PER_DATA.decode()))

if __name__ == "__main__":
    print(DATA_PROCESSED)
