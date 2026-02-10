from typing import Any, Optional, List, Union, Dict, Protocol
from abc import ABC, abstractmethod


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage():
    """
    pour dictionnaire:
    dict = {} pour le cree
    pour le remplir il faut faire:
    dict_data = {"valeur": data}
    valeur est la cle pour avoir acce data dans un bibliotheque
    """
    def process(self, data: Any) -> Dict:
        dict_data = {"validate": True, "valeur": data}
        return dict_data
