# Example function for toolkit integration

def detect_keystream_reuse_xor(c1: bytes, c2: bytes) -> bytes:
    """
    Return c1 XOR c2.

    If c1 and c2 were encrypted with the same stream cipher keystream,
    this equals p1 XOR p2 and may leak information about both plaintexts.
    """
    return xor_bytes(c1, c2)