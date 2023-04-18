#!/usr/bin/python3
"""This module provides a function for writing a string to a file."""

def write_to_file(file_path: str, text: str) -> int:
    """Writes a string to a text file and returns the number of characters written."""
    with open(file_path, "w", encoding="utf-8") as file:
        num_chars_written = file.write(text)
    return num_chars_written

