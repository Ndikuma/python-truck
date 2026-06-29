from itertools import permutations

def drinks_water():
    """Return the nationality of the person who drinks water."""
    return solve_puzzle()[0]


def owns_zebra():
    """Return the nationality of the person who owns the zebra."""
    return solve_puzzle()[1]


def solve_puzzle():
    """Solve the Zebra Puzzle and return (water_drinker, zebra_owner)."""
    # Define all possible values
    colors = ['red', 'green', 'ivory', 'yellow', 'blue']
    nationalities = ['Englishman', 'Spaniard', 'Ukrainian', 'Norwegian', 'Japanese']
    pets = ['dog', 'snails', 'fox', 'horse', 'zebra']
    drinks = ['coffee', 'tea', 'milk', 'orange_juice', 'water']
    hobbies = ['dancing', 'painting', 'reading', 'football', 'chess']
    
    # Iterate over all permutations
    for color_perm in permutations(colors):
        # Statement 10: Norwegian lives in the first house
        for nat_perm in permutations(nationalities):
            if nat_perm[0] != 'Norwegian':
                continue
            
            # Statement 2: Englishman lives in the red house
            if nat_perm[color_perm.index('red')] != 'Englishman':
                continue
            
            # Statement 11: Norwegian lives next to the blue house
            if abs(color_perm.index('blue') - nat_perm.index('Norwegian')) != 1:
                continue
            
            for pet_perm in permutations(pets):
                # Statement 3: Spaniard owns the dog
                if pet_perm[nat_perm.index('Spaniard')] != 'dog':
                    continue
                
                for drink_perm in permutations(drinks):
                    # Statement 5: Ukrainian drinks tea
                    if drink_perm[nat_perm.index('Ukrainian')] != 'tea':
                        continue
                    
                    # Statement 4: Person in green house drinks coffee
                    if drink_perm[color_perm.index('green')] != 'coffee':
                        continue
                    
                    # Statement 6: Green house is immediately to the right of ivory house
                    if color_perm.index('green') != color_perm.index('ivory') + 1:
                        continue
                    
                    # Statement 9: Person in middle house drinks milk
                    if drink_perm[2] != 'milk':
                        continue
                    
                    for hobby_perm in permutations(hobbies):
                        # Statement 7: Snail owner likes dancing
                        if hobby_perm[pet_perm.index('snails')] != 'dancing':
                            continue
                        
                        # Statement 8: Person in yellow house is a painter
                        if hobby_perm[color_perm.index('yellow')] != 'painting':
                            continue
                        
                        # Statement 13: Football player drinks orange juice
                        if drink_perm[hobby_perm.index('football')] != 'orange_juice':
                            continue
                        
                        # Statement 14: Japanese person plays chess
                        if hobby_perm[nat_perm.index('Japanese')] != 'chess':
                            continue
                        
                        # Statement 12: Painter's house is next to the horse
                        if abs(color_perm.index('yellow') - pet_perm.index('horse')) != 1:
                            continue
                        
                        # Statement 11: Reading person lives next to the fox
                        if abs(hobby_perm.index('reading') - pet_perm.index('fox')) != 1:
                            continue
                        
                        # All conditions satisfied! Find the answers
                        water_drinker = nat_perm[drink_perm.index('water')]
                        zebra_owner = nat_perm[pet_perm.index('zebra')]
                        return water_drinker, zebra_owner
    
    return None, None