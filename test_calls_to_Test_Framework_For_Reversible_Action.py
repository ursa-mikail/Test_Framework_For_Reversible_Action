from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
import os


# Example cipher and decipher functions for testing
def example_cipher(text):
    return ''.join(chr((ord(char) + 1) % 256) for char in text),

def example_decipher(text):
    return ''.join(chr((ord(char) - 1) % 256) for char in text)

# AES-GCM-256 Cipher and Decipher
def example_cipher_aes_gcm256(data_hex):
    key = os.urandom(32)  # 256-bit key
    iv = os.urandom(12)  # 96-bit IV for GCM
    data = bytes.fromhex(data_hex)
    
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=default_backend()
    ).encryptor()
    
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return (ciphertext.hex(), key.hex(), iv.hex(), encryptor.tag.hex())

def example_decipher_aes_gcm256(data_hex, key_hex, iv_hex, tag_hex):
    key = bytes.fromhex(key_hex)
    iv = bytes.fromhex(iv_hex)
    tag = bytes.fromhex(tag_hex)
    data = bytes.fromhex(data_hex)
    
    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag),
        backend=default_backend()
    ).decryptor()
    
    return (decryptor.update(data) + decryptor.finalize()).hex()

# RSA-OAEP Cipher and Decipher
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def example_cipher_rsa_oaep(data_hex, public_key):
    data = bytes.fromhex(data_hex)
    ciphertext = public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return (ciphertext.hex(),)

def example_decipher_rsa_oaep(data_hex, private_key):
    data = bytes.fromhex(data_hex)
    plaintext = private_key.decrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.hex()

# Example usage
if __name__ == "__main__":
    # Generate RSA keys
    private_key, public_key = generate_rsa_keys()
    
    # Initialize the framework
    framework = Test_Framework_For_Reversible_Action()

    # Add tests for AES-GCM-256 and RSA-OAEP functions
    framework.add_test(
        "AES-GCM-256",
        example_cipher_aes_gcm256,
        example_decipher_aes_gcm256,
        ["48656c6c6f20776f726c64", "4a6f686e20446f65"]  # data series
    )
    framework.add_test(
        "RSA-OAEP-2048",
        lambda data: example_cipher_rsa_oaep(data, public_key),
        lambda data: example_decipher_rsa_oaep(data, private_key),
        ["48656c6c6f20776f726c64", "4a6f686e20446f65"]  # data series
    )

    # Add a test for the example cipher/decipher functions
    framework.add_test(
        "Random cipher",
        lambda data: example_cipher(data),
        lambda data: example_decipher(data),
        ["hello", "world", "1234", "!@#$"]  # data series
    )

    # Run the tests
    framework.run_tests()

"""
Running Test 1: AES-GCM-256
Test passed for input: 48656c6c6f20776f726c64
Test passed for input: 4a6f686e20446f65
===== Running Test 1: AES-GCM-256 [DONE] =====
Running Test 2: RSA-OAEP-2048
Test passed for input: 48656c6c6f20776f726c64
Test passed for input: 4a6f686e20446f65
===== Running Test 2: RSA-OAEP-2048 [DONE] =====
Running Test 3: Random cipher
Test passed for input: hello
Test passed for input: world
Test passed for input: 1234
Test passed for input: !@#$
===== Running Test 3: Random cipher [DONE] =====
"""