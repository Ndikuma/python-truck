from itertools import combinations
from math import lcm

def sum_of_multiples(limit, factors):
    if limit <= 0:
        return 0
    
    valid_factors = [f for f in factors if 0 < f < limit]
    
    if not valid_factors:
        return 0
    
    total_sum = 0
    
    # Use inclusion-exclusion principle
    # For each subset of factors, add or subtract the sum of multiples of their LCM
    for k in range(1, len(valid_factors) + 1):
        for combo in combinations(valid_factors, k):
            # Calculate LCM of the combination
            current_lcm = 1
            for factor in combo:
                current_lcm = lcm(current_lcm, factor)
                if current_lcm >= limit:
                    break
            
            if current_lcm >= limit:
                continue
            
            # Number of multiples of current_lcm less than limit
            n = (limit - 1) // current_lcm
            
            # Sum of arithmetic series: n * (first + last) / 2
            sum_of_multiples = n * (current_lcm + n * current_lcm) // 2
            
            # Add or subtract based on subset size (inclusion-exclusion)
            if k % 2 == 1:
                total_sum += sum_of_multiples
            else:
                total_sum -= sum_of_multiples
    
    return total_sum