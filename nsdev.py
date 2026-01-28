import binascii
import hashlib
import base64

class CipherHandler:
    def __init__(self, method="bytes", key=None):
        self.method = method
        # Multi-layer obfuscated key generation
        if key is None:
            _p1 = base64.b64decode("UGVyZmVjdA==").decode()  
            _p2 = base64.b64decode("UGFzcw==").decode()     
            _temp = _p1 + _p2
            
            # Layer 3: Dynamic key derivation using system properties
            _salt = str(hash("nsdev") % 999999).encode()
            _derived = hashlib.pbkdf2_hmac('sha256', _temp.encode(), _salt, 1000)
            
            # Layer 4: Use first 16 bytes for consistency
            key = _derived[:16]
        
        self.key = key.encode() if isinstance(key, str) else key
    
    def decrypt(self, encrypted_hex):
        """Decrypt hex-encoded XOR encrypted data"""
        try:
            # Convert hex to bytes
            encrypted_data = binascii.unhexlify(encrypted_hex)
            
            # XOR decrypt
            result = bytearray()
            key_len = len(self.key)
            for i, byte in enumerate(encrypted_data):
                result.append(byte ^ self.key[i % key_len])
            
            return bytes(result).decode('utf-8')
        except Exception as e:
            raise RuntimeError(f"Decryption failed: {e}")
