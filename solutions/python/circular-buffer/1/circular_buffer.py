class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # Initialize buffer with None placeholders
        self.buffer = [None] * capacity
        self.read_ptr = 0
        self.size = 0

    def read(self):
        if self.size == 0:
            raise BufferEmptyException("Circular buffer is empty")
        
        # Read the oldest data
        data = self.buffer[self.read_ptr]
        self.buffer[self.read_ptr] = None  # Clear slot
        
        # Move read pointer forward circularly
        self.read_ptr = (self.read_ptr + 1) % self.capacity
        self.size -= 1
        return data

    def write(self, data):
        if self.size == self.capacity:
            raise BufferFullException("Circular buffer is full")
        
        # Calculate write pointer based on read pointer and current size
        write_ptr = (self.read_ptr + self.size) % self.capacity
        self.buffer[write_ptr] = data
        self.size += 1

    def overwrite(self, data):
        if self.size < self.capacity:
            # If there's space, it behaves exactly like a regular write
            self.write(data)
        else:
            # If full, overwrite the oldest data (at read_ptr)
            self.buffer[self.read_ptr] = data
            # The overwritten data is gone, so the NEXT element becomes the oldest
            self.read_ptr = (self.read_ptr + 1) % self.capacity
            # Size remains equal to capacity

    def clear(self):
        self.buffer = [None] * self.capacity
        self.read_ptr = 0
        self.size = 0