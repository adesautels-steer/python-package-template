"""Core module of sample_package."""

from . import helpers


def main() -> None:
    """Greets the user and notes the current time."""
    print(f"Hello from sample_package at {helpers.get_current_time()}.")
