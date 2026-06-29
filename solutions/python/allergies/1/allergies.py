class Allergies:
    def __init__(self, score):
        self.score = score
        self.allergens = {
            'eggs': 1,
            'peanuts': 2,
            'shellfish': 4,
            'strawberries': 8,
            'tomatoes': 16,
            'chocolate': 32,
            'pollen': 64,
            'cats': 128
        }

    def allergic_to(self, item):
        """Check if the person is allergic to a specific item."""
        if item not in self.allergens:
            return False
        return (self.score & self.allergens[item]) != 0

    @property
    def lst(self):
        """Return a list of all allergens the person is allergic to."""
        return [item for item in self.allergens 
                if self.score & self.allergens[item]]

    # Alternative implementation with a list for better ordering
    @property
    def lst_ordered(self):
        """Return allergens in the order they are listed."""
        allergen_list = ['eggs', 'peanuts', 'shellfish', 'strawberries', 
                        'tomatoes', 'chocolate', 'pollen', 'cats']
        return [item for item in allergen_list 
                if self.score & self.allergens[item]]