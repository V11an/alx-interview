#!/usr/bin/python3

"""

UTF-8 Validation

"""


def validUTF8(data):
    """
    This function checks if a list of integers represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing bytes of data.

    Returns:
        True if the data is valid UTF-8 encoding, False otherwise.
    """
    num_bytes_expected = 0  # Tracks the number of expected continuation bytes

    for byte in data:
        # Extract the 8 least significant bits representing the actual byte data
        byte = byte & 0b11111111

        # Check for single-byte characters (starting with 0)
        if num_bytes_expected == 0:
            if byte >> 7 == 0:  # Single-byte character (ASCII)
                continue
            elif byte >> 5 == 0b110:  # 2-byte character (first byte)
                num_bytes_expected = 1
            elif byte >> 4 == 0b1110:  # 3-byte character (first byte)
                num_bytes_expected = 2
            elif byte >> 3 == 0b11110:  # 4-byte character (first byte)
                num_bytes_expected = 3
            else:  # Invalid starting byte
                return False
        # Check for continuation bytes (starting with 10)
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes_expected -= 1  # Decrement for each valid continuation byte

        # Check if all multi-byte sequences are complete
        return num_bytes_expected == 0

        # Example usage (place this in a separate file like 0-main.py)
        if __name__ == "__main__":
            validUTF8 = __import__('0-validate_utf8').validUTF8

        data = [65]  # 'A' (single-byte)
        print(validUTF8(data))

        data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]  # "This is cool!" (ASCII)
        print(validUTF8(data))

        data = [229, 65, 127, 256]  # Invalid byte value (256)
        print(validUTF8(data))
