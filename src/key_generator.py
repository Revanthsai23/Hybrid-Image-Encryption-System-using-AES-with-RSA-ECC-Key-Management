import hashlib
import os
import secrets
import time
import numpy as np

class KeyGenerator:

    def __init__(self):
        initial_entropy = str(time.time()).encode() + os.urandom(16)
        self.state = hashlib.sha256(initial_entropy).digest()

    def feed_entropy(self, source):
        combined = bytes([a ^ b for a, b in zip(self.state, source)])
        self.state = hashlib.sha256(combined).digest()

    def generate_key(self, size=32):
        if size > 32:
            raise ValueError("Maximum key size is 32 bytes")
        random_bytes = secrets.token_bytes(size)
        
        self.feed_entropy(random_bytes)
    
        return self.state[:size]