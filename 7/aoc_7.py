#poker karty pro part 1 (druhé zakomentovat)
#poker_cards = {"A" : 1, "K" : 2, "Q" : 3, "J" : 4, "T" : 5, "9" : 6, "8" : 7, "7" : 8, "6" : 9, "5" : 10, "4" : 11, "3" : 12, "2" : 13}
#poker karty pro part 2 (druhé zakomentovat)
poker_cards = {"A" : 1, "K" : 2, "Q" : 3, "T" : 4, "9" : 5, "8" : 6, "7" : 7, "6" : 8, "5" : 9, "4" : 10, "3" : 11, "2" : 12, "J" : 13}
poker_hands = {
    "poker" : 1,
    "4kind" : 2,
    "fullhouse" : 3,
    "3kind" : 4,
    "2pairs" : 5,
    "pair" : 6,
    "empty_hand" : 7
}
hands_bids = {}
part1 = 0
used_hands = []


""" funkce pro part 1(nutne druhou zakomentovat)
def get_poker_hand(poker):
    for card in poker_cards:
        fullhouse, two_pairs = False, False
        if poker.count(card) == 5:
            return "poker"
        elif poker.count(card) == 4:
            return "4kind"
        elif poker.count(card) == 3:
            for card2 in poker_cards:
                if poker.count(card2) == 2 and card != card2:
                    fullhouse = True
                    return "fullhouse"
            return "3kind"
        elif poker.count(card) == 2:
            for card2 in poker_cards:
                if poker.count(card2) == 2 and card != card2:
                    two_pairs = True
                    return "2pairs"
                elif poker.count(card2) == 3 and card != card2:
                    fullhouse = True
                    return "fullhouse"
            if not two_pairs: return "pair"
    return "empty_hand"
    """

# funkce pro part 2 (nutne druhou zakomentovat)
def get_poker_hand(poker):
    for card in poker_cards:
        fullhouse, two_pairs = False, False
        if poker.count(card) == 5:
            return "poker"
        elif poker.count(card) == 4:
            if "J" in poker:
                return "poker"
            return "4kind"
        elif poker.count(card) == 3:
            for card2 in poker_cards:
                if poker.count(card2) == 2 and card != card2:
                    fullhouse = True
                    if "J" in poker:
                        return "poker"
                    return "fullhouse"
            if "J" in poker:
                return "4kind"        
            return "3kind"
        elif poker.count(card) == 2:
            for card2 in poker_cards:
                if poker.count(card2) == 2 and card != card2:
                    two_pairs = True
                    if "J" in poker:
                        if poker.count("J") == 2:
                            return "4kind"
                        return "fullhouse"
                    return "2pairs"
                elif poker.count(card2) == 3 and card != card2:
                    fullhouse = True
                    if "J" in poker:
                        return "poker"
                    return "fullhouse"
            if "J" in poker:
                return "3kind"
            if not two_pairs: return "pair"
    if "J" in poker:
        return "pair"
    return "empty_hand"

def second_rule(new, new_bid, old, old_bid):
    for j in range(len(new)):
        if poker_cards[new[j]] != poker_cards[old[j]]:
            if poker_cards[new[j]] > poker_cards[old[j]]: return new, new_bid
            else: return old, old_bid
                    
with open('input_2.txt') as f:
    lines = f.readlines()
    for l in lines:
        split = l.split()
        hands_bids[split[0]] = int(split[1])
        
    for i in range(len(lines)):
        lowest_hand_rank = 0
        lowest_hand = "00000"
        lowest_hand_bid = 0
        for line in lines:    
            splitted = line.split()
            rank = get_poker_hand(splitted[0])
            if poker_hands[rank] == lowest_hand_rank and splitted[0] not in used_hands:
                lowest_hand_rank = poker_hands[rank]
                lowest_hand, lowest_hand_bid = second_rule(splitted[0], int(splitted[1]), lowest_hand, lowest_hand_bid)
            elif poker_hands[rank] > lowest_hand_rank and splitted[0] not in used_hands:
                lowest_hand_rank = poker_hands[rank]
                lowest_hand = splitted[0]
                lowest_hand_bid = int(splitted[1])
                
        used_hands.append(lowest_hand)
    for index in range(len(used_hands)):
        print("hand no:",index+1,  used_hands[index])

    ind = 1
    for h in used_hands:
        part1 += hands_bids[h]*(ind)
        ind += 1
        
print("PART1:", part1)