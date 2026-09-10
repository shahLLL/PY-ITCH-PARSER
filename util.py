from __future__ import annotations

def read_uint48(data: bytes) -> int:
    """Read 6-byte big-endian unsigned integer (timestamp)."""
    return int.from_bytes(data, byteorder="big")


def parse_price(raw: int) -> float:
    """Convert ITCH price (integer) to float dollars."""
    return raw / 10000.0