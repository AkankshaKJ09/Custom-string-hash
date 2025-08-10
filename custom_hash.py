def custom_hash(input_str, hash_length=32):
    if not input_str:
        input_str = ""
    
    # Initialize variables with prime numbers
    hash_value = 5381
    prime1 = 33
    prime2 = 0x811C9DC5  # FNV prime
    
    # Process each character
    for i, char in enumerate(input_str):
        # Get ASCII value and apply transformations
        ascii_val = ord(char)
        shifted_val = ((ascii_val << (i % 7)) | (ascii_val >> (8 - (i % 7))))  # Circular shift
        xor_val = shifted_val ^ (i * prime1)
        
        # Mix with hash value using modular arithmetic
        hash_value = ((hash_value * prime2) ^ xor_val) & 0xFFFFFFFF
    
    # Convert to bytes for further processing
    hash_bytes = hash_value.to_bytes(4, 'big')
    
    # Additional mixing with input length
    length_factor = len(input_str) % 256
    mixed_bytes = bytes((b + length_factor + i) % 256 for i, b in enumerate(hash_bytes * 8))
    
    # Final compression to desired length
    final_hash = ""
    for i in range(hash_length):
        # Select bytes and combine them
        byte_index = (i * 7) % len(mixed_bytes)
        combined = (mixed_bytes[byte_index] + mixed_bytes[(byte_index + 3) % len(mixed_bytes)]) % 256
        
        # Convert to hex character
        final_hash += f"{combined:02x}"[0 if i % 2 else 1]
    
    return final_hash[:hash_length]