from abc import ABC, abstractmethod


class Strategy(ABC):

    def __init__(self) -> None:
        super().__init__()

    def evaluateDecision(self) -> bool:
        pass