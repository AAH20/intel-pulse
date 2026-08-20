import urllib.request
import xml.etree.ElementTree as ET
import html
import re
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class FeedItem:
    title: str
    link: str
    summary: str
    source_name: str
    category: str
    published: str = ""

class RSSFetcher:
    """
    Standard-library zero-dependency asynchronous/sync XML RSS and Atom feed parser.
    """
    def __init__(self, timeout_s: int = 10):
        self.timeout_s = timeout_s

    def _clean_html(self, raw_html: str) -> str:
        clean = re.sub(r'<.*?>', '', raw_html)
        return html.unescape(clean).strip()

    def fetch_feed(self, source_name: str, url: str, category: str) -> List[FeedItem]:
        items: List[FeedItem] = []
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "IntelPulse/1.0 (+https://github.com/AAH20/intel-pulse)"}
            )
            with urllib.request.urlopen(req, timeout=self.timeout_s) as response:
                content = response.read()

            root = ET.fromstring(content)

            # RSS 2.0
            channel = root.find("channel")
            if channel is not None:
                for item in channel.findall("item"):
                    title_elem = item.find("title")
                    link_elem = item.find("link")
                    desc_elem = item.find("description")
                    pub_elem = item.find("pubDate")

                    title = title_elem.text if title_elem is not None and title_elem.text else "No Title"
                    link = link_elem.text if link_elem is not None and link_elem.text else ""
                    summary = self._clean_html(desc_elem.text) if desc_elem is not None and desc_elem.text else ""
                    pub = pub_elem.text if pub_elem is not None and pub_elem.text else ""

                    items.append(FeedItem(
                        title=title.strip(),
                        link=link.strip(),
                        summary=summary[:300] + ("..." if len(summary) > 300 else ""),
                        source_name=source_name,
                        category=category,
                        published=pub
                    ))

            # Atom Feeds
            for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
                title_elem = entry.find("{http://www.w3.org/2005/Atom}title")
                link_elem = entry.find("{http://www.w3.org/2005/Atom}link")
                summary_elem = entry.find("{http://www.w3.org/2005/Atom}summary")
                content_elem = entry.find("{http://www.w3.org/2005/Atom}content")
                updated_elem = entry.find("{http://www.w3.org/2005/Atom}updated")

                title = title_elem.text if title_elem is not None and title_elem.text else "No Title"
                link = link_elem.attrib.get("href", "") if link_elem is not None else ""
                
                raw_text = ""
                if summary_elem is not None and summary_elem.text:
                    raw_text = summary_elem.text
                elif content_elem is not None and content_elem.text:
                    raw_text = content_elem.text
                
                summary = self._clean_html(raw_text)
                pub = updated_elem.text if updated_elem is not None and updated_elem.text else ""

                items.append(FeedItem(
                    title=title.strip(),
                    link=link.strip(),
                    summary=summary[:300] + ("..." if len(summary) > 300 else ""),
                    source_name=source_name,
                    category=category,
                    published=pub
                ))

        except Exception as e:
            # Resilient fallback: feed failure doesn't break entire pipeline
            print(f"[WARN] Failed to fetch feed '{source_name}' ({url}): {e}")

        return items
