def score(x, y):
    # Calculate the distance from the center (0, 0)
    distance = (x**2 + y**2) ** 0.5
    
    # 1. Inner circle: radius <= 1
    if distance <= 1:
        return 10
        
    # 2. Middle circle: radius <= 5
    if distance <= 5:
        return 5
        
    # 3. Outer circle: radius <= 10
    if distance <= 10:
        return 1
        
    # 4. Outside the target
    return 0