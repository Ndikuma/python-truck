def is_paired(input_string):
    # Map each closing bracket to its matching opening bracket
    matching_bracket = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    # Track the opening brackets we encounter
    stack = []
    
    for char in input_string:
        # If it's an opening bracket, push it onto the stack
        if char in matching_bracket.values():
            stack.append(char)
            
        # If it's a closing bracket, verify it matches the top of the stack
        elif char in matching_bracket:
            # If the stack is empty, we have a closing bracket with no opening pair
            if not stack:
                return False
                
            # Pop the top element and see if it matches
            top_element = stack.pop()
            if matching_bracket[char] != top_element:
                return False
                
        # Any other characters (letters, numbers, spaces) are completely ignored
        
    # If the stack is empty, all pairs matched perfectly.
    # If anything is left in the stack, an opening bracket was never closed!
    return len(stack) == 0