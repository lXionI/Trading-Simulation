from src.strategy import Strategy

from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd


class SimulationDuration():

    def __init__(self, 
                 start_date: str,
                 end_date: str) -> None:
        self.start_date = pd.to_datetime(start_date)
        self.end_date = pd.to_datetime(end_date)

        if self.start_date > self.end_date:
            raise ValueError(f"Start Date exceeds End Date. {self.start_date} > {self.end_date}")


class SimulationResults():

    def __init__(self) -> None:
        pass


class Simulation(ABC):

    def __init__(self,
                 path_stock_data: Path | str, 
                 duration: SimulationDuration,
                 budget: float=100.0,
                 seperator: str=";") -> None:
        super().__init__()
        if type(path_stock_data) == str:
            path_stock_data = Path(path_stock_data)
        path_stock_date = path_stock_data.resolve()
        if not path_stock_date.is_file():
            raise ValueError(f"Following path: {path_stock_date} is not a file.")
        self.df_stock = pd.read_csv(path_stock_data, sep=seperator)
        # ensure that the Date field is in datetime format
        self.df_stock.loc[:, "Date"] = self.df_stock.loc[:, "Date"].apply(lambda x: pd.to_datetime(x))
        self.duration = duration
        self.budget = budget


    def run(self, strategy: Strategy=None) -> SimulationResults:
        df_sim_start = self.df_stock.loc[:, "Date"] >= self.duration.start_date
        df_sim_end = self.df_stock.loc[:, "Date"] <= self.duration.end_date

        df_sim = self.df_stock[df_sim_start & df_sim_end]

        for ds_sim in df_sim.loc[:, "Date"]:
            # start of day - Open - allow to sell for open prices / buy on next day if no shares are available?
            print(f"Current trading day: {ds_sim}")
            # apply strategy
            # adjust money
            
            # End of day - Close - allow to buy for open prices / sell and buy next day