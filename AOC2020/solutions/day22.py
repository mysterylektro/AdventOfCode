from collections import deque


def compute_winning_score(winning_deck):
    return sum([(i + 1) * val for i, val in enumerate(reversed(list(winning_deck)))])


def combat(decks, recursion=False):
    prev_states = set()
    while all(len(deck) != 0 for deck in decks):
        if recursion and tuple([tuple(deck) for deck in decks]) in prev_states:
            return 0, decks[0]
        prev_states.add(tuple([tuple(deck) for deck in decks]))
        cards = [deck.popleft() for deck in decks]
        if recursion:
            if all([len(deck) >= card for card, deck in zip(cards, decks)]):
                winner = combat([deque(list(deck)[:card]) for card, deck in zip(cards, decks)], recursion=True)[0]
            else:
                winner = cards.index(max(cards))
        else:
            winner = cards.index(max(cards))
        cards.insert(0, cards.pop(winner))
        decks[winner].extend(cards)

    winner, winning_deck = None, None
    for i, deck in enumerate(decks):
        if len(deck) > 0:
            winner, winning_deck = i, deck
            break
    return winner, winning_deck


inputs = open('../inputs/day22.txt').read().split('\n\n')
player_decks = [deque(list(map(int, [card.strip() for card in i.split('\n')[1:] if card != '']))) for i in inputs]
print(f'Part 1 Answer: {compute_winning_score(combat([deck.copy() for deck in player_decks])[1])}')
print(f'Part 2 Answer: {compute_winning_score(combat([deck.copy() for deck in player_decks], recursion=True)[1])}')
