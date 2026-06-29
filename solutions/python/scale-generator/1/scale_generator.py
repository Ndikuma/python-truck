class Scale:
    def __init__(self, tonic):
        # Preserve input case for minor key identification
        self.tonic = tonic
        # Capitalize only for index lookup in the scale lists
        lookup_tonic = tonic[0].upper() + tonic[1:]
        
        self.sharps = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        self.flats = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
        
        # Determine sharp/flat scale
        # Keys using flats: F, Bb, Eb, Ab, Db, Gb, d, g, c, f, bb, eb
        flat_keys = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb', 'eb']
        
        if self.tonic in flat_keys:
            self.chromatic_notes = self.flats
        else:
            self.chromatic_notes = self.sharps
            
        # Ensure the tonic lookup uses the capitalized version to match self.chromatic_notes
        self.tonic_lookup = lookup_tonic

    def chromatic(self):
        """Return the chromatic scale starting from the tonic."""
        tonic_index = self.chromatic_notes.index(self.tonic_lookup)
        return self.chromatic_notes[tonic_index:] + self.chromatic_notes[:tonic_index]

    def interval(self, intervals):
        """Return the scale based on the given interval pattern."""
        chromatic = self.chromatic()
        result = [chromatic[0]]
        position = 0
        
        interval_steps = {'m': 1, 'M': 2, 'A': 3}
        
        for interval in intervals:
            position = (position + interval_steps[interval]) % len(chromatic)
            result.append(chromatic[position])
        
        return result