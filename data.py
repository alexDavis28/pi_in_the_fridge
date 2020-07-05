import pandas as pd
from config import CSV_PATH
import csv
import matplotlib.pyplot as plt

def init_csv(filename):
    data = {
        "datetime": [],
        "temperature": []
    }
    df = pd.DataFrame(data)
    df.to_csv(filename)
    print("Created csv")


def append_data(datetime: str = None, temperature: float = None):
    data = {
        "datetime": [datetime],
        "temperature": [temperature]
    }
    df = pd.DataFrame(data)
    try:
        df.to_csv(CSV_PATH, mode='a', header=False)
    except FileNotFoundError:
        print("File not found, sorry")
    print("Added data to file")


def wipe_csv(filename):
    data = {
        "datetime": [],
        "temperature": []
    }
    df = pd.DataFrame(data)
    df.to_csv(filename)
    print("Wiped csv")


def graph(filename):

    x = []
    y = []

    with open(filename, 'r') as file:
        plots = csv.reader(file, delimiter=",")
        for row in plots:
            x.append(row[0])
            y.append(float(row[1]))

    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Change in temperature over time")
    plt.legend()
    plt.show()
