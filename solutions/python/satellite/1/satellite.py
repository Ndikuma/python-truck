class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tree_from_traversals(preorder, inorder):
    # --- empty tree case ---
    if not preorder and not inorder:
        return {}

    # --- validation: must match expected error messages ---
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")

    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")

    # Validation (keeping your existing logic)
    if len(preorder) != len(inorder) or set(preorder) != set(inorder):
        raise ValueError("Invalid traversals")

    index_map = {v: i for i, v in enumerate(inorder)}
    pre_index = 0

    def build(left, right):
        nonlocal pre_index
        if left > right:
            return None

        root_val = preorder[pre_index]
        pre_index += 1
        root = Node(root_val)
        mid = index_map[root_val]
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root

    def node_to_dict(node):
        """Helper to convert Node object to the expected dictionary format."""
        if node is None:
            return {}
        return {
            "v": node.value,
            "l": node_to_dict(node.left),
            "r": node_to_dict(node.right)
        }

    root_node = build(0, len(inorder) - 1)
    return node_to_dict(root_node)