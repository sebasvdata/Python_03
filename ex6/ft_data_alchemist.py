import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    players_list = ['Alice', 'bob', 'Charlie',
                    'dylan', 'Emma', 'Gregory',
                    'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players_list}")

    capitalized_list = [player.capitalize() for player in players_list]
    print(f"New list with all names capitalized: {capitalized_list}")

    only_capitalized = [player for player in players_list
                        if player == player.capitalize()]
    print(f"New list of capitalized names only: {only_capitalized}")

    players_dict = {player: random.randint(0, 1000)
                    for player in capitalized_list}
    print(f"Score dict: {players_dict}")

    score_avg = round(sum(players_dict.values()) / len(capitalized_list), 2)
    print(f"Score average is {score_avg}")

    high_scores = {player: score for player, score in players_dict.items()
                   if score > score_avg}
    print(f"High scores: {high_scores}")
