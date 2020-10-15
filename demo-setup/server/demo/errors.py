# -*- coding:utf-8 -*-


class UnsupportedPlatformError(Exception):
    """Raised when the platform Hermes Audio Server is running on is not
    supported."""

    def __init__(self, platform):
        """Initialize the exception with a string representing the platform."""
        self.platform = platform
