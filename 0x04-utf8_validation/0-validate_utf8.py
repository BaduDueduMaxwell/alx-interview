#!/usr/bin/python3
"""  UTF-8 Validation """


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    :param data: List of integers representing bytes of data.
    :return: True if data is valid UTF-8 encoding, False otherwise.
    """
    remaining_bytes = 0

    for byte in data:
        byte = byte & 0xFF

        if remaining_bytes == 0:
            if (byte >> 7) == 0:
                continue
            elif (byte >> 5) == 0b110:
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:
                remaining_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1

    return remaining_bytes == 0
