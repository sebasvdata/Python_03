import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players: tuple[str, ...] = ("charlie", "dylan", "alice", "bob")
    actions: tuple[str, ...] = ("move", "grab", "climb",
                                "use", "release", "swim")
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
        event_list: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:

    while event_list:
        i = random.randint(0, len(event_list) - 1)
        yield event_list.pop(i)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    event_list: list[tuple[str, str]] = []
    event_generator = gen_event()
    for event_num in range(1000):
        event = next(event_generator)
        print(f"Event {event_num}: "
              f"Player {event[0]} did action {event[1]}")

    for i in range(0, 10):
        event_list.append(next(event_generator))

    print(f"Built list of 10 events: {event_list}")
    for event_pop in consume_event(event_list):
        print(f"Got event from list: {event_pop}")
        print(f"Remains in list: {event_list}")
