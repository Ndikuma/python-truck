def maximum_value(maximum_weight, items):
    # Handle base cases where knapsack has no capacity or there are no items
    if maximum_weight == 0 or not items:
        return 0
        
    n = len(items)
    
    # Create a 2D table initialized with 0s
    # Rows: items considered (0 to n)
    # Columns: capacities (0 to maximum_weight)
    dp = [[0] * (maximum_weight + 1) for _ in range(n + 1)]
    
    # Populate the table bottom-up
    for i in range(1, n + 1):
        # Access item attributes from the object (assuming objects with attributes or dicts)
        # We can handle both class instances (item.weight) or dictionaries (item['weight']) safely
        item = items[i - 1]
        weight = item.weight if hasattr(item, 'weight') else item.get('weight', 0)
        value = item.value if hasattr(item, 'value') else item.get('value', 0)
        
        for w in range(maximum_weight + 1):
            if weight <= w:
                # Store the maximum of including vs. excluding the current item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                # If the item is too heavy, skip it and carry over the previous maximum
                dp[i][w] = dp[i - 1][w]
                
    # The bottom-right cell holds the maximum total value possible
    return dp[n][maximum_weight]