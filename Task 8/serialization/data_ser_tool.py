# This is task 8
""" 8. Custom Data Serialization Tool
 ● Description    : Develop a tool to convert data between different formats (e.g., JSON,
                   XML, and custom-defined formats) without using libraries.
 ● Challenges     :
                    ○ Parseand generate structured data in different formats.
                    ○ Create a schema validator for consistency.
                    ○ Handle edge cases like nested structures or invalid data.
 ● Skills         : String parsing, recursion, and algorithm design.
 8. Custom Data Serialization Tool
                    ● Restriction: Only custom formats (no use of JSON, XML, or other predefined formats).
                    ● Reason:The objective here is for students to understand data serialization by creating
                    their own custom formats. Using JSON or XML would shortcut the process and miss the
                    key concepts of converting data structures into a serialized form. This project focuses on
                    understanding how data can be stored in simple text formats and how to design a parser
                    for custom formats.
                    ● Learning Outcome: Students will understand how to serialize data, build custom
                    parsers, and create efficient data storage methods, which is a crucial concept in data
                    transfer and file-based applications."""
import re

class CustomSerializer:
    def __init__(self):
        self.delimiter = "|"
        self.key_value_sep = ":"
        self.list_start = "["
        self.list_end = "]"

    def serialize(self, data):
        """Convert Python dictionary/list into a custom format string."""
        if isinstance(data, dict):
            serialized_data = []
            for key, value in data.items():
                serialized_value = self.serialize(value)
                serialized_data.append(f"{key}{self.key_value_sep}{serialized_value}")
            return self.delimiter.join(serialized_data)

        elif isinstance(data, list):
            serialized_list = self.delimiter.join(self.serialize(item) for item in data)
            return f"{self.list_start}{serialized_list}{self.list_end}"

        elif isinstance(data, (int, float)):  # Handle numbers
            return f"#{data}"  # Prefix numbers with #

        elif isinstance(data, str):  # Handle strings safely
            return f"\"{data}\""  # Enclose strings in quotes

        else:
            raise ValueError("Unsupported data type")

    def deserialize(self, data):
        """Convert custom format string back into a Python dictionary/list."""
        if data.startswith(self.list_start) and data.endswith(self.list_end):
            return self._parse_list(data)

        elif self.key_value_sep in data:
            return self._parse_dict(data)

        elif data.startswith("\"") and data.endswith("\""):  # Handle string
            return data[1:-1]

        elif data.startswith("#"):  # Handle numbers
            return int(data[1:]) if "." not in data else float(data[1:])

        else:
            return data  # Return as-is if not recognized

    def _parse_list(self, data):
        """Helper function to parse a serialized list."""
        inner_data = data[1:-1]  # Remove brackets
        items = self._smart_split(inner_data, self.delimiter)
        return [self.deserialize(item) for item in items]

    def _parse_dict(self, data):
        """Helper function to parse a serialized dictionary."""
        elements = self._smart_split(data, self.delimiter)
        deserialized_data = {}
        for element in elements:
            if self.key_value_sep in element:
                key, value = element.split(self.key_value_sep, 1)
                deserialized_data[key] = self.deserialize(value)
        return deserialized_data

    def _smart_split(self, data, delimiter):
        """Splits while preserving quoted strings and nested structures."""
        parts = []
        current = []
        inside_quotes = False
        depth = 0  # For tracking nested lists

        for char in data:
            if char == "\"" and (not current or current[-1] != "\\"):
                inside_quotes = not inside_quotes
            elif char == self.list_start:
                depth += 1
            elif char == self.list_end:
                depth -= 1

            if char == delimiter and not inside_quotes and depth == 0:
                parts.append("".join(current))
                current = []
            else:
                current.append(char)

        if current:
            parts.append("".join(current))

        return parts

# Example Usage
serializer = CustomSerializer()

# Sample Dictionary with Nested Structures
sample_data = {
    "name": "John",
    "age": 30,
    "skills": ["Python", "C++", "Java"],
    "address": {"city": "New York", "zip": "10001"},
    "salary": 5000.50
}

# Serialization
serialized_string = serializer.serialize(sample_data)
print("Serialized:", serialized_string)

# Deserialization
deserialized_data = serializer.deserialize(serialized_string)
print("Deserialized:", deserialized_data)

