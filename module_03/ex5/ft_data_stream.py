#!/usr/bin/env python3

import random
import typing

players = ['Alice', 'Bob', 'Dylan', 'Charlie']
actions = ['run', 'eat', 'sleep', 'grab', 'climb', 'swim', 'move', 'release']

def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield random.choice(players), random.choice(actions)

def consume_event(events: list[tuple[str, str]]) -> typing.Generator[tuple[str, str], None, None]:
    while len(events):
        random_item = random.choice(events)
        events.remove(random_item)
        yield random_item
    
def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()

    for i in range(1000):
        player, action = next(gen_event())
        print(f"Event {i}: Player {player} did action {action}")

    tuples_list = []
    for i in range(10):
        player, action = next(event_generator)
        tuples_list.append((player, action))
        
    print(f"Built list of 10 events: {tuples_list}")

    for item in consume_event(tuples_list):
        print("Got event from the list:", item)
        print("Remains in list:", tuples_list)
 
if __name__ == '__main__':
    main()