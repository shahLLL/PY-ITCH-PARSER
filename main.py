from __future__ import annotations
import struct
import sys
from typing import Optional, Iterator
from pathlib import Path
from parser import parse_message, big_endian_2_byte_format_str
from dataclass import *

TYPE_TO_LEN_MAP: dict[str, int] = {
    'S': 12,
    'R': 39,
    'H': 25,
    'Y': 20,
    'L': 26,
    'V': 35,
    'W': 12,
    'K': 28,
    'J': 35,
    'h': 21,
    'A': 36,
    'F': 40,
    'E': 31,
    'C': 36,
    'X': 23,
    'D': 19,
    'U': 35,
    'P': 44,
    'Q': 40,
    'B': 19,
    'I': 50,
    'O': 48,
}

def iter_messages(filename: str | Path, max_messages: Optional[int] = None) -> Iterator[Message]:
    """
    Yield parsed messages from an ITCH file.
    Automatically detects length-prefixed vs raw format.
    """
    path = Path(filename)
    data = path.read_bytes()
    pos = 2
    count = 0

    length_prefixed = False
    if len(data) >= 2:
        first_len = struct.unpack_from(big_endian_2_byte_format_str, data, 0)[0]
        if 8 <= first_len <= 64:
            length_prefixed = True

    while pos < len(data):
        if max_messages is not None and count >= max_messages:
            break

        if length_prefixed:
            if pos + 2 > len(data):
                break
            msg_len = struct.unpack_from(big_endian_2_byte_format_str, data, pos)[0]
            pos += 2
            if pos + msg_len > len(data):
                break
            msg = data[pos:pos + msg_len]
            pos += msg_len
        else:
            if pos >= len(data):
                break
            msg_type = chr(data[pos])
            msg_len = TYPE_TO_LEN_MAP.get(msg_type)
            if msg_len is None:
                print(f"Unknown message type '{msg_type}' at offset {pos}. Stopping.")
                break
            if pos + msg_len > len(data):
                break
            msg = data[pos:pos + msg_len]
            pos += msg_len

        parsed = parse_message(msg)
        if parsed is not None:
            yield parsed
            count += 1

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <itch_file> [max_messages]")
        sys.exit(1)

    filename = sys.argv[1]
    max_msgs = int(sys.argv[2]) if len(sys.argv) > 2 else 40

    print(f"Parsing: {filename}")
    print("-" * 80)

    for i, msg in enumerate(iter_messages(filename, max_messages=max_msgs), 1):
        print("Message #{}: {}".format(i, msg))
    print("-" * 80)
    print("Done.")
    print("PY-ITCH-PARSER")

if __name__ == "__main__":
    main()