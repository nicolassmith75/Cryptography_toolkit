"""
Educational block cipher helper functions for CYBR 3570.

WARNING:
These helpers are for learning and demonstration. Do not use this module as a
complete production encryption library.
"""

from cryptography.hazmat.primitives import padding


def blocks(data: bytes, block_size: int = 16) -> list[bytes]:
    """Split bytes into block-sized chunks."""
    return [data[i:i + block_size] for i in range(0, len(data), block_size)]


def show_blocks(data: bytes, block_size: int = 16) -> str:
    """Return blocks as space-separated hex strings."""
    return " ".join(block.hex() for block in blocks(data, block_size))


def xor_bytes(a: bytes, b: bytes) -> bytes:
    """XOR two byte strings up to the shorter length."""
    return bytes(x ^ y for x, y in zip(a, b))


def hamming_distance(a: bytes, b: bytes) -> int:
    """Count differing bits between two byte strings of equal length."""
    if len(a) != len(b):
        raise ValueError("Inputs must have equal length")
    return sum((x ^ y).bit_count() for x, y in zip(a, b))


def pkcs7_pad(data: bytes, block_size_bits: int = 128) -> bytes:
    """Apply PKCS#7 padding."""
    padder = padding.PKCS7(block_size_bits).padder()
    return padder.update(data) + padder.finalize()


def pkcs7_unpad(data: bytes, block_size_bits: int = 128) -> bytes:
    """Remove PKCS#7 padding."""
    unpadder = padding.PKCS7(block_size_bits).unpadder()
    return unpadder.update(data) + unpadder.finalize()
