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
        for i in data:
            if not isinstance(i, int):
                return False
        return "Numeric data verified"

    def process(self, data: None) -> str:
        datat = []
        for i in data:
            datat.append(i)
        return f"{datat}"

    def format_output(self, data: None) -> str:
        return (f"Output: Processed {len(data)} "
                f"numeric values, sum={sum(data)}, avg={sum(data)/len(data)}")


class TextProcessor(DataProcessor):
    def process(self, data: None) -> str:
        return f"'{data}'"

    def validate(self, data: None) -> bool:
        if isinstance(data, str):
            return False
        return True

    def format_output(self, data: None) -> str:
        tab = []
        for i in data.split(" "):
            tab.append(i)
        return (f"Output: Processed text: {len(data)} "
                f"characters, {len(tab)} words")


class LogProcessor(DataProcessor):
    def process(self, data: None) -> str:
        return data.split("ERROR: ")[1]

    def validate(self, data: None) -> bool:
        if isinstance(data, str) and "ERROR" in data:
            return "Log entry verified"
        return False

    def format_output(self, data: None) -> str:
        return f"[ALERT] ERROR level detected: {data}"


def polymorphique_fonc(type: object, data: None):
    print("Processing data:", type.process(data))
    print("Validation: ", type.validate(data))
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
    print("Result 3:", log.format_output("System ready"))
    print("\nFoundation systems online. Nexus ready for advanced streams")
