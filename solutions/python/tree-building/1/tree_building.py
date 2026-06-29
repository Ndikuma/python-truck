class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records:
        return None
    
    # Sort by record_id
    records.sort(key=lambda r: r.record_id)
    
    # Validate: records must be continuous from 0 to n-1
    for i, record in enumerate(records):
        if record.record_id != i:
            raise ValueError('Record id is invalid or out of order.')
    
    # Create all nodes
    nodes = {record.record_id: Node(record.record_id) for record in records}
    
    # Build the tree
    root = None
    for record in records:
        if record.record_id == 0:
            # Root must have parent_id == 0
            if record.parent_id != 0:
                raise ValueError('Node parent_id should be smaller than its record_id.')
            root = nodes[0]
        else:
            # Parent ID must be less than record ID
            if record.parent_id >= record.record_id:
                # Check if it's a self-reference (cycle)
                if record.parent_id == record.record_id:
                    raise ValueError('Only root should have equal record and parent id.')
                raise ValueError('Node parent_id should be smaller than its record_id.')
            nodes[record.parent_id].children.append(nodes[record.record_id])
    
    return root