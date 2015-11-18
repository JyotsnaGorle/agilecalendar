from Crypto.Cipher import AES
import base64
import hashlib
import json
import agilecalendar.settings as settings


class SessionKeygen:

    def __init__(self):
        self.BLOCK_SIZE = 32
        self.PADDING = '{'
        self.key = settings.SECRET_KEY
        self.cipher = AES.new(hashlib.sha256(self.key).digest())

    def _pad(self, block):
        return block + (self.BLOCK_SIZE - len(block) % self.BLOCK_SIZE) * self.PADDING

    def _encrypt(self, plain_text):
        return base64.b64encode(self.cipher.encrypt(self._pad(plain_text)))

    def _decrypt(self, cipher_text):
        return self.cipher.decrypt(base64.b64decode(cipher_text)).rstrip(self.PADDING)

    def get_key(self, username, ip, time):
        plain_text = "{'username': %s, 'ip': %s, 'time': %s}" % (username, ip, time)
        return self._encrypt(plain_text)

    def get_info(self, cipher_text):
        return json.loads(self._decrypt(cipher_text))
