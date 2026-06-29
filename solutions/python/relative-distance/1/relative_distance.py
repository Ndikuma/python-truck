class RelativeDistance:
    def __init__(self, family_tree):
        self.family_tree = family_tree
        self.graph = {}
        
        # Build undirected graph from family tree
        for parent, children in family_tree.items():
            # Add parent if not exists
            if parent not in self.graph:
                self.graph[parent] = set()
            
            # Add each child and connect both ways
            for child in children:
                if child not in self.graph:
                    self.graph[child] = set()
                self.graph[parent].add(child)
                self.graph[child].add(parent)
            
            # Connect siblings to each other
            for i in range(len(children)):
                for j in range(i + 1, len(children)):
                    child1 = children[i]
                    child2 = children[j]
                    self.graph[child1].add(child2)
                    self.graph[child2].add(child1)

    def degree_of_separation(self, person_a, person_b):
        # Validate inputs
        if person_a not in self.graph:
            raise ValueError("Person A not in family tree.")
        if person_b not in self.graph:
            raise ValueError("Person B not in family tree.")
        
        # If same person
        if person_a == person_b:
            return 0
        
        # BFS for shortest path
        from collections import deque
        
        visited = {person_a}
        queue = deque([(person_a, 0)])
        
        while queue:
            current, distance = queue.popleft()
            
            for relative in self.graph[current]:
                if relative == person_b:
                    return distance + 1
                
                if relative not in visited:
                    visited.add(relative)
                    queue.append((relative, distance + 1))
        
        # No path found
        raise ValueError("No connection between person A and person B.")