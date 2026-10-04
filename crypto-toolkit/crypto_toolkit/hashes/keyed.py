# Starter code for crypto_toolkit/hashes/keyed.py

MODULE_STARTER = """

#Module: crypto_toolkit.hashes.keyed

#Educational keyed hashing utilities for CYBR 3570.

#WARNING
-------
These wrappers are for learning. Production applications should rely on
well-reviewed libraries and protocol-level constructions.
"""

import hashlib
import hmac


def sha256_digest(message: bytes) -> bytes:
    """Return SHA-256(message)."""
    return hashlib.sha256(message).digest()


def hmac_sha256(key: bytes, message: bytes) -> bytes:
    """Return HMAC-SHA-256(key, message)."""
    return hmac.new(key, message, hashlib.sha256).digest()


def verify_hmac_sha256(key: bytes, message: bytes, tag: bytes) -> bool:
    """Verify HMAC-SHA-256 using constant-time comparison."""
    expected = hmac_sha256(key, message)
    return hmac.compare_digest(expected, tag)


print(MODULE_STARTER)