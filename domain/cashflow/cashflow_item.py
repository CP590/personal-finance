from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class CashFlowItem(ABC):
    id: str
    name: str

    @abstractmethod
    def annual_amount(self) -> float:
        pass

    @abstractmethod
    def monthly_amount(self) -> float:
        pass
