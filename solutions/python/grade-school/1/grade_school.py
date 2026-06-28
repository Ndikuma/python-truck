class School:
    def __init__(self):
        # Maps grade (int) -> set of student names (strings)
        self._roster = {}
        # Tracks whether a student is already registered anywhere in the school
        self._all_students = set()
        # A list to keep track of operations results for validation tests
        self._added_log = []

    def add_student(self, name, grade):
        # Check if the student is already enrolled anywhere in the school
        if name in self._all_students:
            self._added_log.append(False)
            return False
        
        # Initialize the grade set if it doesn't exist yet
        if grade not in self._roster:
            self._roster[grade] = set()
            
        # Add the student to the grade and global tracking
        self._roster[grade].add(name)
        self._all_students.add(name)
        self._added_log.append(True)
        return True

    def grade(self, grade_number):
        # Return a sorted list of students in the requested grade
        # If the grade doesn't exist, return an empty list
        return sorted(list(self._roster.get(grade_number, [])))

    def roster(self):
        # Get a sorted list of all students in all grades.
        # Grades are sorted numerically, and students within each grade are sorted alphabetically.
        full_roster = []
        for grade in sorted(self._roster.keys()):
            full_roster.extend(self.grade(grade))
        return full_roster

    def added(self):
        # Some test frameworks look for a log of true/false results 
        # indicating if the consecutive add operations succeeded.
        return self._added_log