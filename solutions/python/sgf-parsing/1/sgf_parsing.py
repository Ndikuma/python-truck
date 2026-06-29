class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        return (self.properties == other.properties and 
                self.children == other.children)


def parse(input_string):
    if not input_string:
        raise ValueError("tree missing")
    
    s = input_string.strip()
    
    if not s.startswith('(') or not s.endswith(')'):
        raise ValueError("tree missing")
        
    if s == "()":
        raise ValueError("tree with no nodes")
        
    tree, pos = _parse_tree(s, 0)
    
    # Ensure we consumed the entire meaningful string
    while pos < len(s) and s[pos].isspace():
        pos += 1
    if pos != len(s):
        raise ValueError("tree missing")
        
    return tree


def _parse_tree(s, pos):
    if pos >= len(s) or s[pos] != '(':
        raise ValueError("tree missing")
    pos += 1  # Skip '('
    
    nodes = []
    while pos < len(s) and s[pos] == ';':
        node, pos = _parse_node_properties(s, pos)
        nodes.append(node)
        
    if not nodes:
        raise ValueError("tree with no nodes")
        
    # Check for variations (children trees)
    children = []
    while pos < len(s) and s[pos] == '(':
        child_tree, pos = _parse_tree(s, pos)
        children.append(child_tree)
        
    if pos >= len(s) or s[pos] != ')':
        raise ValueError("tree missing")
    pos += 1  # Skip ')'
    
    # In SGF, a sequence of nodes (;A;B;C) means A -> B -> C. 
    # We construct the tree from the tail of the sequence backwards.
    current_tree = nodes[-1]
    current_tree.children = children
    
    for i in range(len(nodes) - 2, -1, -1):
        nodes[i].children = [current_tree]
        current_tree = nodes[i]
        
    return current_tree, pos


def _parse_node_properties(s, pos):
    pos += 1  # Skip ';'
    properties = {}
    
    while pos < len(s) and s[pos] not in (';', '(', ')'):
        if s[pos].isspace():
            pos += 1
            continue
            
        key, pos = _parse_key(s, pos)
        if not key.isupper():
            raise ValueError("property must be in uppercase")
            
        values = []
        while pos < len(s) and s[pos] == '[':
            value, pos = _parse_value(s, pos + 1)
            values.append(value)
            
        if not values:
            raise ValueError("properties without delimiter")
            
        properties[key] = values
        
    return SgfTree(properties=properties), pos


def _parse_key(s, pos):
    start = pos
    while pos < len(s) and s[pos] != '[':
        if s[pos] in (';', '(', ')'):
            raise ValueError("properties without delimiter")
        pos += 1
    if pos == len(s):
        raise ValueError("properties without delimiter")
    return s[start:pos], pos


def _parse_value(s, pos):
    result = []
    escaped = False
    
    while pos < len(s):
        char = s[pos]
        
        if char == ']' and not escaped:
            return _clean_text(''.join(result)), pos + 1
            
        if char == '\\' and not escaped:
            escaped = True
            pos += 1
            continue
            
        if escaped:
            if char == '\n':
                pass  # SGF spec: escaped newlines are removed completely
            else:
                result.append(char)
            escaped = False
        else:
            result.append(char)
            
        pos += 1
        
    raise ValueError("properties without delimiter")


def _clean_text(text):
    result = []
    for c in text:
        if c == '\n':
            result.append('\n')
        elif c.isspace():
            result.append(' ')
        else:
            result.append(c)
    return ''.join(result)