from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self) -> str:
        pass

    @abstractmethod
    def validate(self) -> bool:
        pass

    @abstractmethod
    def format_output(self) -> str:
        pass


class NumericProcessor(DataProcessor):
    def validate(self, data: None) -> bool:
        if isinstance(data, int):
            return True
        return False

    def process(self, data: None) -> str:
        datat = []
        for i in data:
            datat.append(int(i))
        return datat

    def format_output(self, data: None) -> str:
        return (f"Output: Processed {len(data)} "
                f"numeric values, sum={sum(data)}, avg={sum(data)/len(data)}")


class TextProcessor(DataProcessor):
    def process(self, data: None) -> str:
        pass

    def validate(self, data: None) -> bool:
        if isinstance(data, str):
            return True
        return False

    def format_output(self, data: None) -> str:
        pass


class LogProcessor(DataProcessor):
    def process(self, data: None) -> str:
        pass

    def validate(self, data: None) -> bool:
        if isinstance(data, int):
            return True
        return False

    def format_output(self, data: None) -> str:
        pass
