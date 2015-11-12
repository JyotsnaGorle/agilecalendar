import string
import random


class SessionKeygen:

    def __init__(self):
        self.generated_keys = []
        self.key_length = 50

    def get_new_key(self):
        while True:
            key = ''.join(random.SystemRandom().choice(
                string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(self.key_length))

            if key not in self.generated_keys:
                self.generated_keys.append(key)
                break

        return key

    def remove_key(self, key):
        self.generated_keys.remove(key)
