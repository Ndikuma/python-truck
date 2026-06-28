from collections import deque

def simulate_game(deck_a, deck_b):
    p1 = deque(deck_a)
    p2 = deque(deck_b)
    pile = []
    
    total_cards_played = 0
    tricks_count = 0
    
    penalties = {'J': 1, 'Q': 2, 'K': 3, 'A': 4}
    seen_states = set()
    
    def get_normalized_state(current_turn, penalty):
        norm_p1 = tuple('N' if str(c) not in penalties else c for c in p1)
        norm_p2 = tuple('N' if str(c) not in penalties else c for c in p2)
        return (norm_p1, norm_p2, current_turn, penalty)

    current_player = 0  # 0 for Player A, 1 for Player B
    penalty_due = 0
    last_face_card_player = None
    
    while True:
        # CRITICAL FIX: Only check and record loop states at the START of a round 
        # (when the pile is empty and a player is about to initiate play)
        if len(pile) == 0:
            state = get_normalized_state(current_player, penalty_due)
            if state in seen_states:
                return {"status": "loop", "cards": total_cards_played, "tricks": tricks_count}
            seen_states.add(state)
        
        active_deck = p1 if current_player == 0 else p2
        opponent_deck = p2 if current_player == 0 else p1
        
        # 1. Edge Case: Active player is out of cards
        if not active_deck:
            opponent_deck.extend(pile)
            tricks_count += 1
            return {"status": "finished", "cards": total_cards_played, "tricks": tricks_count}
            
        # 2. Player rolls a card to the table
        card = active_deck.popleft()
        pile.append(card)
        total_cards_played += 1
        
        # 3. Process Card Impact
        if str(card) in penalties:
            penalty_due = penalties[str(card)]
            last_face_card_player = current_player
            current_player = 1 - current_player
        else:
            if penalty_due > 0:
                penalty_due -= 1
                if penalty_due == 0:
                    winner_deck = p1 if last_face_card_player == 0 else p2
                    winner_deck.extend(pile)
                    pile = []
                    tricks_count += 1
                    
                    if not p1 or not p2:
                        return {"status": "finished", "cards": total_cards_played, "tricks": tricks_count}
                        
                    current_player = last_face_card_player
                    last_face_card_player = None
                else:
                    continue
            else:
                current_player = 1 - current_player