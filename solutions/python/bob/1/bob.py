def response(hey_bob):
    # 1. Clean up the input by removing whitespace from the ends
    phrase = hey_bob.strip()
    
    # 2. Check for silence (empty string)
    if not phrase:
        return "Fine. Be that way!"
        
    # 3. Check if the input is yelled (has letters, and all of them are uppercase)
    is_yelling = phrase.isupper()
    
    # 4. Check if the input is a question (ends with a question mark)
    is_question = phrase.endswith("?")
    
    # 5. Bob's logic rules
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."