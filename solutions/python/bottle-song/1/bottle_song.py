def recite(start, take=1):
    # Word lists for numbers
    numbers = ["no", "one", "two", "three", "four", "five", 
               "six", "seven", "eight", "nine", "ten"]
    numbers_cap = ["No", "One", "Two", "Three", "Four", "Five", 
                   "Six", "Seven", "Eight", "Nine", "Ten"]
    
    verses = []
    
    for i in range(take):
        current = start - i
        next_count = current - 1
        
        # Format current line
        if current == 1:
            current_text = f"{numbers_cap[current]} green bottle"
        else:
            current_text = f"{numbers_cap[current]} green bottles"
        
        # Format next line
        if next_count == 1:
            next_text = f"{numbers[next_count]} green bottle"
        elif next_count == 0:
            next_text = f"{numbers[next_count]} green bottles"
        else:
            next_text = f"{numbers[next_count]} green bottles"
        
        verse = [
            f"{current_text} hanging on the wall,",
            f"{current_text} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {next_text} hanging on the wall."
        ]
        
        verses.extend(verse)
        
        if i < take - 1:
            verses.append("")
    
    return verses