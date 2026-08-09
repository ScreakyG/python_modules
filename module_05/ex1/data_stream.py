#!/usr/bin/env python3
import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._internal_storage: list[str] = []
        self._rank: int = -1
        self._processed: int = 0
    
    def output(self) -> tuple[int, str]:
        oldest_item = self._internal_storage.pop(0)
        self._rank += 1
        return self._rank, oldest_item
    
    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass
        
    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

class TextProcessor(DataProcessor):
    
    def validate(self, data: typing.Any) -> bool:

        if not isinstance(data, (str, list)):
            return False
        
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False

        return True

    def ingest(self, data: str | list[str]) -> None:

        if self.validate(data) == False:
            raise Exception("Improprer text data")
        
        if isinstance(data, list):
            for item in data:
                self._internal_storage.append(item)
                self._processed += 1

        elif isinstance(data, str):
            self._internal_storage.append(data)
            self._processed += 1

class LogProcessor(DataProcessor):
    
    def validate(self, data: typing.Any) -> bool:

        if not isinstance(data, (dict, list)):
                return False
        
        if isinstance(data, dict):
            return all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )

        for item in data:
            if not isinstance(item, dict):
                return False
    
            for key, value in item.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False

        return True

    def ingest(self, data: dict | list[dict]) -> None:

        if self.validate(data) == False:
            raise Exception("Improprer dict data")
        
        if isinstance(data, list):
            for item in data:
                values = ",".join([value for value in item.values()])
                self._internal_storage.append(str(values))
                self._processed += 1

        elif isinstance(data, dict):
            values = ",".join([value for value in data.values()])
            self._internal_storage.append(values)
            self._processed += 1


class NumericProcessor(DataProcessor):
    
    def validate(self, data: typing.Any) -> bool:

        if isinstance(data, (int, float, list)) == False:
            return False
        
        if isinstance(data, list):
            for item in data:
                if isinstance(item, (int, float)) == False:
                    return False

        return True

    def ingest(self, data: int | float | list[int | float]) -> None:

        if self.validate(data) == False:
            raise Exception("Improprer numeric data")
        
        if isinstance(data, list):
            for item in data:
                self._internal_storage.append(str(item))
                self._processed += 1

        elif isinstance(data, (int, float)):
            self._internal_storage.append(str(data))
            self._processed += 1


class DataStream:
    def __init__(self) -> None:
        self._processor_list: list[DataProcessor] = []
    
    def register_processor(self, proc: DataProcessor) -> None:
        self._processor_list.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for data in stream:
            for processor in self._processor_list:
                if processor.validate(data):
                    processor.ingest(data)
                    break
            else:
                print(f"DataStream error - Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        
        if len(self._processor_list) == 0:
            print("No processor found, no data")

        else:
            for processor in self._processor_list:
                print(f"{type(processor).__name__}: total {processor._processed} items processed, remaining {len(processor._internal_storage)} on processor")

def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")

    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()

    stream = DataStream()
    stream.print_processors_stats()

    data = [
                'Hello world',
                [3.14, -1, 2.71],
                [
                    {
                        'log_level': 'WARNING',
                        'log_message': 'Telnet access! Use ssh instead'
                    },
                    {
                        'log_level': 'INFO',
                        'log_message': 'User wil is connected'
                    }
                ], 
                42,
                ['Hi', 'five']
            ]

    print("\nRegistering Numeric Processor\n")
    print(f"Sending first batch of data on stream: {data}\n")

    stream.register_processor(numeric_processor)
    stream.process_stream(data)
    stream.print_processors_stats()
    
    print("\nRegistering other data processors")
    stream.register_processor(text_processor)
    stream.register_processor(log_processor)
    print("Send the same batch again")

    stream.process_stream(data)
    stream.print_processors_stats()

    print("\nConsume some elements from the data processors: Numeric 3, Text 2, Log 1")

    for i in range(3):
        numeric_processor.output()

    for i in range(2):
        text_processor.output()

    for i in range(1):
        log_processor.output()

    
    stream.print_processors_stats()


if __name__ == "__main__":
    main()