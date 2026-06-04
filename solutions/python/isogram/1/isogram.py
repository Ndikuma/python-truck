def is_isogram(string):
    # 1. Convert the string to lowercase and filter out non-alphabet characters
    letters = [char for char in string.lower() if char.isalpha()]
    
    # 2. Compare the length of unique letters to the total length of letters
    return len(set(letters)) == len(letters)