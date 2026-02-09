from abc import ABC, abstractmethod
from typing import Any, Optional, List, Union, Dict


class DataStream(ABC):
    def __init__(self, stream_id):
        super().__init__()
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        trier = []
        for i in data_batch:
            if criteria in str(i):
                trier.append(i)
        return trier

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        dictionaire = {"id": self.stream_id}
        return dictionaire


class SensorStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        