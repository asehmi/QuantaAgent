"""String Utilities Module"""


class StringUtils:
    """String Utilities Class"""

    @staticmethod
    def end_slash_remove(line: str) -> str:
        """Remove the ending slash from a line."""

        return line.replace("\\\n", "")

    @staticmethod
    def add_filename_suffix(filename: str, suffix: str) -> str:
        """Inject a suffix into a filename."""

        parts = filename.split(".")
        if len(parts) == 1:  # No file extension
            return f"{filename}{suffix}"
        else:
            return f"{'.'.join(parts[:-1])}{suffix}.{parts[-1]}"
