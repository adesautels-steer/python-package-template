"""Helpers module of sample_package."""

from datetime import datetime


def get_current_time() -> str:
    "Returns the current time."
    return datetime.now().strftime("%-I:%M %p")
