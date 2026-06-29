class Zipper:
    def __init__(self, node, path=None):
        self.node = node
        self.path = path or []

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def value(self):
        return self.node["value"]

    def left(self):
        if self.node["left"] is None:
            return None

        return Zipper(
            self.node["left"],
            self.path + [(self.node, "left")]
        )

    def right(self):
        if self.node["right"] is None:
            return None

        return Zipper(
            self.node["right"],
            self.path + [(self.node, "right")]
        )

    def up(self):
        if not self.path:
            return None

        parent, direction = self.path[-1]
        path = self.path[:-1]

        # rebuild parent node
        if direction == "left":
            new_parent = {
                "value": parent["value"],
                "left": self.node,
                "right": parent["right"],
            }
        else:
            new_parent = {
                "value": parent["value"],
                "left": parent["left"],
                "right": self.node,
            }

        return Zipper(new_parent, path)

    def set_value(self, value):
        new_node = dict(self.node)
        new_node["value"] = value
        return Zipper(new_node, self.path)

    def set_left(self, left):
        new_node = dict(self.node)
        new_node["left"] = left
        return Zipper(new_node, self.path)

    def set_right(self, right):
        new_node = dict(self.node)
        new_node["right"] = right
        return Zipper(new_node, self.path)

    def to_tree(self):
        z = self
        while z.up() is not None:
            z = z.up()
        return z.node