import hashlib
import time
import matplotlib.pyplot as plt
import binascii
import sys

import random
import string

# Timer function to measure execution time
def time_hash_function(hash_func, data):
    start_time = time.time()
    hash_func(data)
    return time.time() - start_time

# Function to generate random hex (N bytes)
def generate_random_hex(n_bytes):
    return binascii.hexlify(bytearray(random.getrandbits(8) for _ in range(n_bytes)))

# Function to generate random ASCII string (N chars)
def generate_random_ascii(n_chars):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(n_chars))

# Example usage
if __name__ == "__main__":
    length_of_input = 100
    n_bytes = length_of_input  # Number of bytes for random hex
    n_chars = length_of_input  # Number of chars for random ASCII

    hex_flag = True  # Flag to toggle between generating hex or ASCII

    # Check if hex encoding should be applied
    if hex_flag:
        # Generate random hex string
        random_hex = generate_random_hex(n_bytes)
        # Decode the hex string
        s1 = random_hex
        print("Generated Random Hex in string:", s1.decode())
        print(f"Random Hex ({n_bytes} bytes):", s1)

    else: # Generate random ASCII string
        random_ascii = generate_random_ascii(n_chars)
        # Encode the ASCII string
        s1 = random_ascii.encode()
        # Convert to hex
        s1 = binascii.hexlify(s1)
        print("Message (in hex bytes):", s1)
        print(f"Random ASCII ({n_chars} chars):", s1.decode())

    # Dictionary to store the timing results
    timing_results = {}

    # List of hashing functions to be tested
    hash_functions = {
        "MD5": hashlib.md5,
        "SHA1": hashlib.sha1,
        "SHA224": hashlib.sha224,
        "SHA256": hashlib.sha256,
        "SHA384": hashlib.sha384,
        "SHA512": hashlib.sha512,
        "SHA3-224": hashlib.sha3_224,
        "SHA3-256": hashlib.sha3_256,
        "SHA3-384": hashlib.sha3_384,
        "SHA3-512": hashlib.sha3_512,
        "Blake2s": hashlib.blake2s,
        "Blake2b": hashlib.blake2b,
        "SHAKE128 (16)": lambda x: hashlib.shake_128(x).hexdigest(16),
        "SHAKE128 (32)": lambda x: hashlib.shake_128(x).hexdigest(32),
        "SHAKE128 (64)": lambda x: hashlib.shake_128(x).hexdigest(64),
        "SHAKE256 (16)": lambda x: hashlib.shake_256(x).hexdigest(16),
        "SHAKE256 (32)": lambda x: hashlib.shake_256(x).hexdigest(32),
        "SHAKE256 (64)": lambda x: hashlib.shake_256(x).hexdigest(64),
    }

    # Measure the time for each hash function
    for hash_name, hash_func in hash_functions.items():
        time_taken = time_hash_function(hash_func, s1)
        timing_results[hash_name] = time_taken
        print(f"{hash_name} took {time_taken:.6f} seconds")

    # Plotting the timings
    names = list(timing_results.keys())
    times = list(timing_results.values())

    plt.figure(figsize=(10, 6))
    plt.barh(names, times, color='skyblue')
    plt.xlabel('Time (seconds)')
    plt.title('Hash Function Execution Time')
    plt.show()

"""
Generated Random Hex in string: e8bb278e9e522b7c4da34dad01083fe9d58a25321c18e8ef4aa8866337f1d9628723dd739b97ecd36b10d86a04c574e2f0730a91aa4b96dc52d075fbb761f4f5fc55e3d4a984d04a5874c75ff51db27385a42fb1dedd9c2f57c07915e2c08113a653661a
Random Hex (100 bytes): b'e8bb278e9e522b7c4da34dad01083fe9d58a25321c18e8ef4aa8866337f1d9628723dd739b97ecd36b10d86a04c574e2f0730a91aa4b96dc52d075fbb761f4f5fc55e3d4a984d04a5874c75ff51db27385a42fb1dedd9c2f57c07915e2c08113a653661a'
MD5 took 0.000010 seconds
SHA1 took 0.000007 seconds
SHA224 took 0.000007 seconds
SHA256 took 0.000003 seconds
SHA384 took 0.000006 seconds
SHA512 took 0.000002 seconds
SHA3-224 took 0.000005 seconds
SHA3-256 took 0.000003 seconds
SHA3-384 took 0.000003 seconds
SHA3-512 took 0.000004 seconds
Blake2s took 0.000006 seconds
Blake2b took 0.000003 seconds
SHAKE128 (16) took 0.000011 seconds
SHAKE128 (32) took 0.000006 seconds
SHAKE128 (64) took 0.000005 seconds
SHAKE256 (16) took 0.000006 seconds
SHAKE256 (32) took 0.000005 seconds
SHAKE256 (64) took 0.000005 seconds
"""
