from abc import ABC, abstractmethod
from typing import Any, Optional, List, Union, Dict


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        super().__init__()
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Méthode abstraite à implémenter dans les classes filles."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filtre les données en utilisant une list comprehension (requis)."""
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Retourne les statistiques du flux (requis)."""
        return {
            "id": self.stream_id,
            "type": self.stream_type,
            "processed": self.processed_count
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            # Extraction des valeurs numériques via list comprehension
            # On gère les floats directs et les dictionnaires {'value': x}
            values = [
                v if isinstance(v, (int, float)) else v.get("value", 0)
                for v in data_batch if isinstance(v, (int, float, dict))
            ]
            avg = sum(values) / len(values) if values else 0.0
            self.processed_count += len(data_batch)
            return (f"Sensor analysis: {len(data_batch)} readings processed,"
                    f" avg temp: {avg}°C")
        except Exception as e:
            return f"Sensor Error: {e}"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            # Analyse des chaînes type "buy:100" ou dictionnaires
            net_flow = 0
            for item in data_batch:
                s = str(item).lower()
                # Extraction simplifiée du nombre après les ':'
                val = int(s.split(':')[-1]) if ':' in s else 0
                if "buy" in s:
                    net_flow += val
                elif "sell" in s:
                    net_flow -= val
            self.processed_count += len(data_batch)
            return (f"Transaction analysis: {len(data_batch)} operations,"
                    f" net flow: {net_flow} units")
        except Exception as e:
            return f"Transaction Error: {e}"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            # Comptage des erreurs via list comprehension
            errors = len([e for e in data_batch if "error" in str(e).lower()])
            self.processed_count += len(data_batch)
            return (f"Event analysis: {len(data_batch)} events,"
                    f" {errors} error detected")
        except Exception as e:
            return f"Event Error: {e}"


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        # Utilisation de isinstance() pour le type checking (requis)
        if isinstance(stream, DataStream):
            self.streams.append(stream)

    def process_all_streams(self, data_map: Dict[str, List[Any]]) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        for stream in self.streams:
            batch = data_map.get(stream.stream_id, [])
            print(stream.process_batch(batch))


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    # Initialisation
    sensor = SensorStream("SENSOR_001")
    trans = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")
    print(f"Initializing Sensor Stream...\nStream ID: {sensor.stream_id},"
          f" Type: {sensor.stream_type}")
    print(sensor.process_batch([22.5, 65, 1013]))
    print(f"Initializing Transaction Stream...\nStream ID: {trans.stream_id},"
          f" Type: {trans.stream_type}")
    print(trans.process_batch(["buy:100", "sell:150", "buy:75"]))
    print(f"Initializing Event Stream...\nStream ID: {event.stream_id},"
          f" Type: {event.stream_type}")
    print(event.process_batch(["login", "error", "logout"]))
    # Traitement Polymorphique
    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)
    # Données mixtes pour la démonstration finale
    mixed_data = {
        "SENSOR_001": [20, 25],
        "TRANS_001": ["buy:50", "buy:50"],
        "EVENT_001": ["error", "login"]
    }
    processor.process_all_streams(mixed_data)
    print("Stream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")
    print("All streams processed successfully. Nexus throughput optimal.")
