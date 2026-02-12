from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        """Format the output string - default implementation"""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        for i in data:
            if not isinstance(i, (int, float)):
                return False
        print("Validation: Numeric data verified")
        return True

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid numeric data"
        total = sum(data)
        avg = total / len(data)
        result = (f"Processed {len(data)} numeric values,"
                  f" sum={total}, avg={avg}")
        return self.format_output(result)


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid text data"
        char_count = len(data)
        word_count = len(data.split())
        result = f"Processed text: {char_count} characters, {word_count} words"
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            print("Validation: Text data verified")
            return True
        return False


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid log entry"
        if "ERROR:" in data:
            message = data.split("ERROR:")[1]
            result = f"[ALERT] ERROR level detected:{message}"
        elif "INFO:" in data:
            message = data.split("INFO:")[1]
            result = f"[INFO] INFO level detected:{message}"
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        if isinstance(data, str) and ("ERROR" in data or "INFO" in data):
            print("Validation: Log entry verified")
            return True
        return False


def polymorphique_fonc(type: object, data: None):
    print("Processing data:", type.process(data))
    print("Output:", type.format_output(data))


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    # 2. TEST NUMERIC PROCESSOR
    print("\nInitializing Numeric Processor...")
    print("Processing data: [1, 2, 3, 4, 5]")
    numb = NumericProcessor()
    print(numb.process([1, 2, 3, 4, 5]))
    # 3. TEST TEXT PROCESSOR
    print("\nInitializing Text Processor...")
    print('Processing data: "Hello Nexus World"')
    text = TextProcessor()
    print(text.process("Hello Nexus World"))
    # 4. TEST LOG PROCESSOR
    print("\nInitializing Log Processor...")
    print('Processing data: "ERROR: Connection timeout"')
    log = LogProcessor()
    print(log.process("ERROR: Connection timeout"))
    # 5. DÉMONSTRATION POLYMORPHIQUE
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
    data_sets = [[1, 2, 3], "Hello Nexus", "INFO: System ready"]
    for i, (processor, data) in enumerate(zip(processors, data_sets), 1):
        result = processor.process(data)
        result_text = result.replace("Output: ", "")
        print(f"Result {i}: {result_text}")
    # 6. MESSAGE FINAL
    print("\nFoundation systems online. Nexus ready for advanced streams.")
