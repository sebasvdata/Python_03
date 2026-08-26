import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players: tuple[str, ...] = ("charlie", "dylan", "alice", "bob")
    actions: tuple[str, ...] = ("move", "grab", "climb",
                                "use", "release", "swim")
    yield (random.choice(players), random.choice(actions))


def consume_event(
        event_list: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    if event_list:
        i = random.randint(0, len(event_list) - 1)
        yield event_list.pop(i)


if __name__ == "__main__":
    event_list: list[tuple[str, str]] = []
    for event_num in range(0, 1001):
        event = next(gen_event())
        print(f"Event {event_num}: "
              f"Player {event[0]} did action {event[1]}")
        event_num += 1

    for i in range(0, 10):
        event = next(gen_event())
        event_list.append(event)

    print(f"Built list of 10 events: {event_list}")
    while event_list:
        event_pop = next(consume_event(event_list))
        print(f"Got event from list: {event_pop}")
        print(f"Remains in list: {event_list}")
