from itertools import combinations as iter_combinations

def combinations(target, size, exclude):
    valid_combinations = []
    
    # 1. Generate all unique combinations of the given 'size' using digits 1-9
    # itertools.combinations naturally prevents duplicate digits within a combination
    for combo in iter_combinations(range(1, 10), size):
        
        # 2. Check if the sum matches our target cage value
        if sum(combo) == target:
            
            # 3. Check if any digit in the combination is in our restricted 'exclude' list
            # We use set intersection for a fast check
            if not any(digit in exclude for digit in combo):
                # Convert tuple to list and append
                valid_combinations.append(list(combo))
                
    return valid_combinations

# --- Testing the Examples ---

# Example 1: 3-digit cage with a sum of 7
print(combinations(7, 3, []))
# Output: [[1, 2, 4]]

# Example 2: 2-digit cage with a sum of 10
print(combinations(10, 2, []))
# Output: [[1, 9], [2, 8], [3, 7], [4, 6]]

# Example 3: 2-digit cage with a sum of 10, excluding [1, 4]
print(combinations(10, 2, [1, 4]))
# Output: [[2, 8], [3, 7]]