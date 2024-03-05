from src.simulation import Simulation, SimulationResults, SimulationDuration
from pathlib import Path

import pandas as pd 
import numpy as np


def main():
    path_data = Path("./data/6PG.SG.csv").resolve()
    duration = SimulationDuration("2019-01-01", "2019-01-31")
    df_data = pd.read_csv(path_data, sep=";")
    df_data.loc[:, "Date"] = df_data.loc[:, "Date"].apply(lambda x: pd.to_datetime(x))


    mask_start = df_data.loc[:, "Date"] >= pd.to_datetime("2019-01-01")
    mask_end = df_data.loc[:, "Date"] <= pd.to_datetime("2019-01-31")

    # print(df_data.loc[mask_start & mask_end])

    Simulation(path_data, duration).run()

if __name__ == "__main__":
    main()