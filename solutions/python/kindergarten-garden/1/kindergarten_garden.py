class Garden:
    DEFAULT_STUDENTS = [
        "Alice", "Bob", "Charlie", "David",
        "Eve", "Fred", "Ginny", "Harriet",
        "Ileana", "Joseph", "Kincaid", "Larry"
    ]

    PLANTS = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets"
    }

    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.rows = diagram.splitlines()
        self.students = sorted(students)

    def plants(self, student):
        index = self.students.index(student)
        start = index * 2

        cups = (
            self.rows[0][start:start + 2] +
            self.rows[1][start:start + 2]
        )

        return [self.PLANTS[plant] for plant in cups]