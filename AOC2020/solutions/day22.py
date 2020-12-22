from collections import deque


def compute_winning_score(winning_deck):
    return sum([(i + 1) * val for i, val in enumerate(reversed(list(winning_deck)))])


def combat(deck1, deck2):
    while len(deck1) != 0 and len(deck2) != 0:
        card1, card2 = deck1.popleft(), deck2.popleft()
        if card1 > card2:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])
    return deck1 if len(deck1) > 0 else deck2


def recursive_combat(deck1, deck2):
    prev_states = set()
    while len(deck1) != 0 and len(deck2) != 0:
        if tuple([tuple(deck1), tuple(deck2)]) in prev_states:
            return 0, deck1
        prev_states.add(tuple([tuple(deck1), tuple(deck2)]))
        card1, card2 = deck1.popleft(), deck2.popleft()
        winner = recursive_combat(deque(list(deck1)[:card1]), deque(list(deck2)[:card2]))[0] if (len(deck1) >= card1 and len(deck2) >= card2) else (0 if card1 > card2 else 1)
        if winner == 0:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])
    return (0, deck1) if len(deck1) > 0 else (1, deck2)


inputs = open('../inputs/day22.txt').read().split('\n\n')
p1_deck = deque(list(map(int, [card.strip() for card in inputs[0].split('\n')[1:]])))
p2_deck = deque(list(map(int, [card.strip() for card in inputs[1].split('\n')[1:-1]])))

print(f'Part 1 Answer: {compute_winning_score(combat(p1_deck.copy(), p2_deck.copy()))}')
print(f'Part 2 Answer: {compute_winning_score(recursive_combat(p1_deck.copy(), p2_deck.copy())[1])}')
