def find_anagrams(target, candidates):
    # Just 4 simple steps!
    
    # Step 1: Sort the letters of our target word
    target_sorted = sorted(target.lower())
    
    # Step 2: Create an empty list for our answers
    result = []
    
    # Step 3: Check each candidate
    for word in candidates:
        # If it's the same word, skip it
        if word.lower() != target.lower():
            # If it has the same sorted letters, it's an anagram
            if sorted(word.lower()) == target_sorted:
                result.append(word)
    
    # Step 4: Give back the anagrams we found
    return result