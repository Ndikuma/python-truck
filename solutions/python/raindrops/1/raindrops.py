def convert(number):
    result = ""
    
    # Check if 3 is a factor
    if number % 3 == 0:
        result += "Pling"
        
    # Check if 5 is a factor
    if number % 5 == 0:
        result += "Plang"
        
    # Check if 7 is a factor
    if number % 7 == 0:
        result += "Plong"
        
    # If result is still empty, return the number as a string
    return result if result else str(number)