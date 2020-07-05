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
    df = pd.read_csv(filename)
    df.plot(kind="line", x="datetime", y="temperature")
    plt.title("Change in temperature over time")
    plt.savefig("graph.png")
    print("Saved graph")
