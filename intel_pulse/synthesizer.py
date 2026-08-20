from typing import List, Dict
from .fetcher import FeedItem

class IntelSynthesizer:
    """
    Deduplicates and synthesizes raw multi-source feed items into
    high-signal executive briefings with problem-solution hooks.
    """
    def deduplicate(self, items: List[FeedItem]) -> List[FeedItem]:
        seen_titles = set()
        unique_items: List[FeedItem] = []
        
        for item in items:
            normalized = "".join(filter(str.isalnum, item.title.lower()))
            if normalized and normalized not in seen_titles:
                seen_titles.add(normalized)
                unique_items.append(item)
                
        return unique_items

    def synthesize(self, items: List[FeedItem], top_k_per_category: int = 3) -> Dict[str, List[FeedItem]]:
        unique_items = self.deduplicate(items)
        categorized: Dict[str, List[FeedItem]] = {}

        for item in unique_items:
            cat = item.category
            if cat not in categorized:
                categorized[cat] = []
            if len(categorized[cat]) < top_k_per_category:
                categorized[cat].append(item)

        return categorized
