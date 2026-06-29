from json import dumps

class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def _build_adj(self, adj):
        """Helper to convert Tree structure into an undirected adjacency list."""
        for child in self.children:
            adj[self.label].append(child.label)
            adj[child.label].append(self.label)
            child._build_adj(adj)

    def _reorient(self, current, parent, adj):
        """Rebuilds the tree structure from an adjacency list."""
        children = []
        for neighbor in adj[current]:
            if neighbor != parent:
                children.append(self._reorient(neighbor, current, adj))
        return Tree(current, children)

    def _find_path(self, current, target, parent, adj, path):
        """DFS to find the unique path between two nodes in a tree."""
        path.append(current)
        if current == target:
            return True
        for neighbor in adj[current]:
            if neighbor != parent:
                if self._find_path(neighbor, target, current, adj, path):
                    return True
        path.pop()
        return False

    def from_pov(self, from_label):
        from collections import defaultdict
        adj = defaultdict(list)
        self._build_adj(adj)
        
        # Check if the requested node actually exists in the tree
        if from_label not in adj and from_label != self.label:
            raise ValueError("Tree could not be reoriented")
            
        return self._reorient(from_label, None, adj)

    def path_to(self, from_label, to_label):
            from collections import defaultdict
            
            adj = defaultdict(list)
            adj[self.label] = [] 
            self._build_adj(adj)
            
            # Validate node existence
            if from_label not in adj:
                raise ValueError("Tree could not be reoriented")
            
            # If the target is missing, the test specifically expects "No path found"
            if to_label not in adj:
                raise ValueError("No path found")
                
            path = []
            if not self._find_path(from_label, to_label, None, adj, path):
                raise ValueError("No path found")
                
            return path