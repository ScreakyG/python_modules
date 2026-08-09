#!/usr/bin/env python3
import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._internal_storage: list[str] = []
        self._rank: int = -1
    
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

        elif isinstance(data, str):
            self._internal_storage.append(data)


class LogProcessor(DataProcessor):
    
    def validate(self, data: typing.Any) -> bool:

        if isinstance(data, (dict, list)) == False:
            return False
        
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) == False:
                    return False

        return True

    def ingest(self, data: dict | list[dict]) -> None:

        if self.validate(data) == False:
            raise Exception("Improprer dict data")
        
        if isinstance(data, list):
            for item in data:
                values = ",".join([value for value in item.values()])
                self._internal_storage.append(str(values))

        elif isinstance(data, dict):
            values = ",".join([value for value in data.values()])
            self._internal_storage.append(values)


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

        elif isinstance(data, (int, float)):
            self._internal_storage.append(str(data))

def test_log_processor() -> None:
    print("Testing Log Processor...")

    test = LogProcessor()
    print(f" Trying to validate input '{42}': {test.validate(42)}")
    print(f" Trying to validate input '{"hello"}': {test.validate("hello")}")

    try:
        print(" Test invalid ingestion of integer '42' without prior validation: ")
        test.ingest(42)
        
    except Exception as error:
        print(" Got exeception:", error)

    try: 
        data = [
            {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
        ]
        print(f" Processing data: {data}")
        test.validate(data)
        print(f" Extracting {len(data)} values...")
        test.ingest(data)

        for item in data:
            rank, item = test.output()
            values = item.split(",")
            print(f" Log entry {rank}: {values[0]}: {values[1]}")
        
    except Exception as error:
        print(" Got exeception:", error)

def test_text_processor() -> None:
    print("Testing Text Processor...")

    test = TextProcessor()
    print(f" Trying to validate input '{42}': {test.validate(42)}")
    print(f" Trying to validate input '{"hello"}': {test.validate("hello")}")

    try:
        print(" Test invalid ingestion of integer '42' without prior validation: ")
        test.ingest(42)
        
    except Exception as error:
        print(" Got exeception:", error)

    try: 
        data = ["Hello", "Nexus", "World"]
        print(f" Processing data: {data}")
        test.validate(data)
        print(f" Extracting {len(data)} values...")
        test.ingest(data)

        for item in data:
            rank, item = test.output()
            print(f" Text value {rank}: {item}")
        
    except Exception as error:
        print(" Got exeception:", error)

def test_numeric_processor() -> None:
    print("Testing Numeric Processor...")

    test = NumericProcessor()
    print(f" Trying to validate input '{42}': {test.validate(42)}")
    print(f" Trying to validate input '{"hello"}': {test.validate("hello")}")

    try:
        print(" Test invalid ingestion of string 'foo' without prior validation: ")
        test.ingest("foo")
        
    except Exception as error:
        print(" Got exeception:", error)

    try: 
        data = [1, 2, 3, 4, 5]
        print(f" Processing data: {data}")
        test.validate(data)
        print(f" Extracting {len(data)} values...")
        test.ingest(data)

        for item in data:
            rank, item = test.output()
            print(f" Numeric value {rank}: {item}")
        
    except Exception as error:
        print(" Got exeception:", error)
        

def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    test_numeric_processor()
    print()
    test_text_processor()
    print()
    test_log_processor()
    
if __name__ == "__main__":
    main()