from typing import Any, List, Union, Dict, Protocol
from abc import ABC, abstractmethod
import time


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Dict[str, Any]:
        ...


class InputStage():
    """
    pour dictionnaire:
    dict = {} pour le cree
    pour le remplir il faut faire:
    dict_data = {"valeur": data}
    valeur est la cle pour avoir acce data dans un bibliotheque
    dans le process:
    On vérifie si data est bien un dictionnaire et n'est pas vide
    On prépare le dictionnaire avec les clés attendues par les autres stages
    Extraction du capteur
    Extraction de la température
    Conservation des données brutes
    Identification du stage
    """
    def process(self, data: Any) -> Dict[str, Any]:
        if data and isinstance(data, dict):
            try:
                return {
                    "validated": True,
                    "sensor": data.get("sensor", "Unknown"),
                    "temp": data.get("temp", 0.0),
                    "data": data,
                    "stage": "input"
                }
            except Exception as e:
                return {"validated": False, "error": str(e), "data": None}
        return {"validated": False, "error": "Invalid or empty data",
                "data": None}


class TransformStage():
    def process(self, data: Any) -> Dict[str, Any]:
        try:
            # Enrichir = ajouter des infos
            return {
                "sensor": data.get("sensor"),
                "temp": data.get("temp"),
                "data": data.get("data"),
                "validated": data.get("validated"),
                "transformed": True,
                "metadata": "enriched with metadata and validation",
                "stage": "transform"
            }
        except Exception as e:
            return {
                "transformed": False,
                "error": str(e),
                "stage": "transform"
            }


class OutputStage():
    def process(self, data: Any) -> Dict[str, Any]:
        try:
            return {
                "formatted": True,
                "result": f"Processed {data.get('sensor')}"
                f"reading: {data.get('temp')}",
                "stage": "output"
            }
        except Exception as e:
            return {"formatted": False, "error": str(e), "stage": "output"}


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        try:
            current_data = data
            for stage in self.stages:
                try:
                    current_data = stage.process(current_data)
                except Exception as stage_error:
                    # Recovery: skip failed stage or use backup
                    print(f"Stage error detected: {stage_error},"
                          f"recovering...")
                    # Continue avec les données actuelles
            return f"[{self.pipeline_id}] {current_data.get('result')}"
        except Exception as e:
            return f"[{self.pipeline_id}] Error: {str(e)}"


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        try:
            current_data = data
            for stage in self.stages:
                try:
                    current_data = stage.process(current_data)
                except Exception as stage_error:
                    # Recovery: skip failed stage or use backup
                    print(f"Stage error detected: {stage_error},"
                          f"recovering...")
                    # Continue avec les données actuelles
            return f"[{self.pipeline_id}] {current_data.get('result')}"
        except Exception as e:
            return f"[{self.pipeline_id}] Error: {str(e)}"


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        try:
            current_data = data
            for stage in self.stages:
                try:
                    current_data = stage.process(current_data)
                except Exception as stage_error:
                    # Recovery: skip failed stage or use backup
                    print(f"Stage error detected: {stage_error},"
                          f"recovering...")
                    # Continue avec les données actuelles
            return f"[{self.pipeline_id}] {current_data.get('result')}"
        except Exception as e:
            return f"[{self.pipeline_id}] Error: {str(e)}"


class NexusManager():
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []
        self.capacity = 1000
        self.records_processed = 0
        self.total_time = 0.0

    def process_all(self, data: Any) -> List[str]:
        start = time.time()
        results = [i.process(data) for i in self.pipelines]
        self.total_time += time.time() - start
        self.records_processed += 1
        return results

    def chain_pipelines(self, pipelines: List[ProcessingPipeline],
                        data: Any) -> str:
        result = data
        for pipeline in pipelines:
            result = pipeline.process(result)
        return result

    def get_stats(self) -> Dict[str, Union[int, float]]:
        efficiency = (self.records_processed /
                      self.total_time * 100) if self.total_time > 0 else 0
        return {
            "records_processed": self.records_processed,
            "total_time": round(self.total_time, 2),
            "efficiency": round(efficiency, 2)}
