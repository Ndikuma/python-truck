import re

def parse(markdown):
    """Convert Markdown to HTML."""
    lines = markdown.split('\n')
    result = []
    in_list = False
    
    for line in lines:
        # Check if the line is a list item
        is_list_item = line.startswith('* ')
        
        # If we are in a list but the current line is NOT a list item, close the list
        if in_list and not is_list_item:
            result.append('</ul>')
            in_list = False
        
        # If we are NOT in a list but the current line IS a list item, start the list
        if not in_list and is_list_item:
            result.append('<ul>')
            in_list = True
            
        result.append(process_line(line, is_list_item))
    
    # Close any open list at the end
    if in_list:
        result.append('</ul>')
    
    return ''.join(result)

def process_line(line, is_list_item):
    """Process a single line of Markdown."""
    # Check for headers
    header_match = re.match(r'(#{1,6}) (.*)', line)
    if header_match:
        level = len(header_match.group(1))
        content = format_inline(header_match.group(2))
        return f'<h{level}>{content}</h{level}>'
    
    # Handle list items
    if is_list_item:
        content = format_inline(line[2:])
        return f'<li>{content}</li>'
    
    # Regular paragraph
    if not line.strip():
        return ''
    line = format_inline(line)
    return f'<p>{line}</p>'

def format_inline(text):
    """Format inline Markdown elements."""
    text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)
    text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)
    return text