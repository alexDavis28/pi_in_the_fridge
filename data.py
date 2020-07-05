import datetime as dt
import pandas as pd
import matplotlib


def init_csv(filename):
    data = {
        "datetime": [],
        "temperature": []
    }
    df = pd.DataFrame(data)
    df.to_csv(filename)