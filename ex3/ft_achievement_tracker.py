import random


def gen_player_achievements(achievements: tuple[str, ...]) -> set[str]:
    player = random.sample(achievements, random.randint(3, 9))
    return set(player)


if __name__ == "__main__":
    achievements: tuple[str, ...] = (
        "First Steps",
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "Unstoppable",
        "Sharp Mind",
        "Hidden Path Finder"
    )

    print("=== Achievement Tracker System ===")

    alice: set[str] = gen_player_achievements(achievements)
    bob: set[str] = gen_player_achievements(achievements)
    charlie: set[str] = gen_player_achievements(achievements)
    dylan: set[str] = gen_player_achievements(achievements)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")

    # '|' could be used as union: alice | bob
    all_achievements = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_achievements}\n")

    # '&' could be used as intersection: alice & bob
    common_achievements = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common_achievements}\n")

    # '-'difference could be used as difference: alice - bob
    only_alice = alice.difference(bob, charlie, dylan)
    only_bob = bob.difference(alice, charlie, dylan)
    only_charlie = charlie.difference(alice, bob, dylan)
    only_dylan = dylan.difference(alice, bob, charlie)

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}\n")

    missing_alice = all_achievements.difference(alice)
    missing_bob = all_achievements.difference(bob)
    missing_charlie = all_achievements.difference(charlie)
    missing_dylan = all_achievements.difference(dylan)

    print(f"Alice is missing: {missing_alice}")
    print(f"Bob is missing: {missing_bob}")
    print(f"Charlie is missing: {missing_charlie}")
    print(f"Dylan is missing: {missing_dylan}")
