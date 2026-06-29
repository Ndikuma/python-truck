class StackUnderflowError(Exception):
    pass


def evaluate(input_data):
    stack = []
    words = {}
    
    # Convert input to list of tokens
    if isinstance(input_data, str):
        tokens = input_data.split()
    else:
        tokens = ' '.join(input_data).split()
    
    i = 0
    while i < len(tokens):
        token = tokens[i].upper()
        
        # Handle word definition
        if token == ':':
            i += 1
            if i >= len(tokens):
                raise ValueError("Malformed definition")
                
            name = tokens[i].upper()
            
            # Check if trying to redefine a number
            try:
                int(name)
                raise ValueError("illegal operation")
            except ValueError as e:
                if str(e) == "illegal operation":
                    raise
            
            i += 1
            definition = []
            while i < len(tokens) and tokens[i] != ';':
                def_token = tokens[i].upper()
                # Expand words immediately at definition time to prevent recursive loops
                if def_token in words:
                    definition.extend(words[def_token])
                else:
                    definition.append(def_token)
                i += 1
                
            if i >= len(tokens) or tokens[i] != ';':
                raise ValueError("Malformed definition")
                
            words[name] = definition
            i += 1
            continue
        
        # Try to parse as number
        try:
            stack.append(int(token))
            i += 1
            continue
        except ValueError:
            pass
        
        # Handle user-defined words
        if token in words:
            # Insert the pre-expanded definition directly into the stream
            tokens = tokens[:i] + words[token] + tokens[i+1:]
            continue
        
        # Stack operations (with explicit underflow validation)
        if token == '+':
            if len(stack) < 2: 
                raise StackUnderflowError("Insufficient number of items in stack")
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)
        elif token == '-':
            if len(stack) < 2: 
                raise StackUnderflowError("Insufficient number of items in stack")
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)
        elif token == '*':
            if len(stack) < 2: 
                raise StackUnderflowError("Insufficient number of items in stack")
            b, a = stack.pop(), stack.pop()
            stack.append(a * b)
        elif token == '/':
            if len(stack) < 2: 
                raise StackUnderflowError("Insufficient number of items in stack")
            b, a = stack.pop(), stack.pop()
            if b == 0:
                raise ZeroDivisionError("divide by zero")
            stack.append(int(a / b))  # Truncates toward zero
        elif token == 'DUP':
            if len(stack) < 1: 
                raise StackUnderflowError("Insufficient number of items in stack")
            stack.append(stack[-1])
        elif token == 'DROP':
            if len(stack) < 1: 
                raise StackUnderflowError("Insufficient number of items in stack")
            stack.pop()
        elif token == 'SWAP':
            if len(stack) < 2: 
                raise StackUnderflowError("Insufficient number of items in stack")
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif token == 'OVER':
            if len(stack) < 2: 
                raise StackUnderflowError("Insufficient number of items in stack")
            stack.append(stack[-2])
        else:
            raise ValueError("undefined operation")
        
        i += 1
        
    return stack