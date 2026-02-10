from abc import ABC, abstractmethod
from typing import Any, Optional, List, Union, Dict


class DataStream(ABC):
    def __init__(self, stream_id):
        super().__init__()
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
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
        try:
            count = len(data_batch)
            avg = 0
            count2 = 0
            for i in data_batch:
                if i.get("type") == "temperature":
                    avg += i.get("value")
                    count2 += 1
            if count2 > 0:
                avg = avg / count2
            else:
                avg = 0
        except Exception as e:
            return str(e)
        return (f"Sensor analysis: {count} readings processed,"
                f" avg temp: {avg} °C")


class TransactionStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            count = len(data_batch)
            sell = 0
            buy = 0
            for i in data_batch:
                if i.get("type") == "buy":
                    buy = buy + i.get("value")
                elif i.get("type") == "sell":
                    sell = sell + i.get("value")
            flux = buy - sell
        except Exception as e:
            return str(e)
        return (f"Transaction analysis: {count} operations,"
                f" net flow: +{flux} units")


class EventStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            count = len(data_batch)
            error = 0
            for i in data_batch:
                if i == "error":
                    error += 1
        except Exception as e:
            return str(e)
        return (f"Event analysis: {count} events,"
                f" {error} error detected")


class StreamProcessor:
    def __init__(self):
        self.streams = []

    def add_stream(self, stream: DataStream):
        self.streams.append(stream)

    def process_all_streams(self, batches: Dict[str, List[Any]]):
        for stream in self.streams:
            try:
                batch_specifique = batches[stream.stream_id]
                print(stream.process_batch(batch_specifique))
            except KeyError:
                print(f"Warning: No batch for {stream.stream_id}")
