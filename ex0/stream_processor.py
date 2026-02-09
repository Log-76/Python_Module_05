from abc import ABC, abstractmethod
from typing import Any


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
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        for i in data:
            if not isinstance(i, int):
                return False
        print("Validation: ", "Numeric data verified")
        return True

    def process(self, data: None) -> str:
        datat = []
        for i in data:
            datat.append(i)
        return f"{datat}"

    def format_output(self, data: Any) -> str:
        try:
            avg = sum(data)/len(data)
            return (f"Output: Processed {len(data)} "
                    f"numeric values, sum={sum(data)}, avg={avg}")
        except ZeroDivisionError:
            return "Error: Empty data"


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def process(self, data: Any) -> str:
        return f"'{data}'"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            print("Validation: Text data verified")
            return True
        return False

    def format_output(self, data: Any) -> str:
        tab = []
        for i in data.split(" "):
            tab.append(i)
        return (f"Output: Processed text: {len(data)} "
                f"characters, {len(tab)} words")


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def process(self, data: Any) -> str:
        try:
            if "ERROR:" in data:
                return data.split("ERROR: ")[1]
            elif "INFO:" in data:
                return data.split("INFO: ")[1]
        except IndexError:
            return "Invalid log format"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str) and ("ERROR" in data or "INFO" in data):
            print("Validation: Log entry verified")
            return True
        return False

    def format_output(self, data: Any) -> str:
        if "ERROR" in data or "ERROR:" in data:
            return f"[ALERT] ERROR level detected: {data}"
        elif "INFO" in data or "INFO:" in data:
            return f"[INFO] INFO level detected: {data}"
        return data


def polymorphique_fonc(type: object, data: None):
    print("Processing data:", type.process(data))
    type.validate(data)
    print("Output:", type.format_output(data))


if __name__ == "__main__":
    numb = NumericProcessor()
    data = [1, 2, 3, 4, 5, 6]
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    polymorphique_fonc(numb, data)
    print()
    print("Initializing Text Processor...")
    text = TextProcessor()
    polymorphique_fonc(text, "Hello Nexus World")
    print()
    print("Initializing Log Processor...")
    log = LogProcessor()
    polymorphique_fonc(log, "ERROR: Connection timeout")
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    print("Result 1:", numb.format_output([1, 2, 3]))
    print("Result 2:", text.format_output("Hello World!"))
    print("Result 3:", log.format_output("INFO: System ready"))
    print("\nFoundation systems online. Nexus ready for advanced streams")
