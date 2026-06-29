class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self.dependents = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if self._value != new_value:
            self._value = new_value
            self._propagate()

    def _propagate(self):
        cells = self._get_dependents_in_order()

        old_values = {cell: cell.value for cell in cells}

        # Recompute everything first
        for cell in cells:
            cell._value = cell.compute_function(
                [inp.value for inp in cell.inputs]
            )

        # Then fire callbacks
        for cell in cells:
            if old_values[cell] != cell.value:
                for callback in cell.callbacks:
                    callback(cell.value)

    def _get_dependents_in_order(self):
        visited = set()
        order = []

        def dfs(cell):
            for dep in cell.dependents:
                if dep not in visited:
                    visited.add(dep)
                    dfs(dep)
                    order.insert(0, dep)

        dfs(self)
        return order
class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = []
        self.dependents = []

        for cell in inputs:
            cell.dependents.append(self)

        self._value = self.compute_function(
            [cell.value for cell in inputs]
        )

    @property
    def value(self):
        return self._value

    def add_callback(self, callback):
        if callback not in self.callbacks:
            self.callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self.callbacks:
            self.callbacks.remove(callback)