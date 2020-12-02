import random
import requests

NUMBER_OF_WINNERS = 3
YEAR = "2020"
LEADERBOARD_ID = "935377"
with open('./aoc_session.txt') as f:
    # Obscuring session ID - Find out how to get your own here: https://github.com/wimglenn/advent-of-code-wim/issues/1
    SESSION_ID = f.readline().strip()

LEADERBOARD_URL = f"https://adventofcode.com/{YEAR}/leaderboard/private/view/{LEADERBOARD_ID}.json"


def parse_members(members_json):
    # Get member name, score and stars
    members = [(m["name"], m["stars"], int(m["last_star_ts"])) for m in members_json.values()]

    # Sort members by stars (highest first), then by last star timestamp (earliest first)
    members.sort(key=lambda s: (-s[1], s[2]))

    # Create a dictionary of member / star values for weighting.
    output = {}
    for member in members:
        output[member[0]] = member[1]

    return output


if __name__ == '__main__':
    r = requests.get(LEADERBOARD_URL, cookies={"session": SESSION_ID})
    participants = parse_members(r.json()['members'])
    print(participants)
    # Create a random seed based on the total number of stars collected by everyone.
    random.seed(sum(participants.values()))
    for i in range(NUMBER_OF_WINNERS):
        # Randomly choose a winner, with each contestant weighted by the number of stars collected.
        winner = random.choices(list(participants.keys()), list(participants.values()))[0]
        # Remove the winner from the pool of winners.
        participants.pop(winner)
        print(f"Winner {i + 1}: {winner}")
