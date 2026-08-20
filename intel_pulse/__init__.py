"""
Intel-Pulse: Autonomous High-Signal AI & Deep-Tech Intelligence Engine.
"""

from .fetcher import FeedItem, RSSFetcher
from .synthesizer import IntelSynthesizer
from .publisher import MarkdownPublisher, EmailHTMLPublisher

__version__ = "0.1.0"
__all__ = [
    "FeedItem",
    "RSSFetcher",
    "IntelSynthesizer",
    "MarkdownPublisher",
    "EmailHTMLPublisher",
]
