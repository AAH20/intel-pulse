import os
import json
import argparse
from .fetcher import RSSFetcher
from .synthesizer import IntelSynthesizer
from .publisher import MarkdownPublisher, EmailHTMLPublisher

def run_pipeline(config_path: str = "config/feeds.json", output_md: str = "LATEST_DIGEST.md", output_html: str = "LATEST_DIGEST.html"):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file '{config_path}' not found.")

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    feeds = config.get("feeds", [])
    print(f"[*] Loaded {len(feeds)} high-signal intelligence feeds.")

    fetcher = RSSFetcher()
    all_items = []

    for feed in feeds:
        print(f"[*] Fetching: {feed['name']} ({feed['url']})...")
        items = fetcher.fetch_feed(
            source_name=feed["name"],
            url=feed["url"],
            category=feed.get("category", "general")
        )
        print(f"    -> Ingested {len(items)} items.")
        all_items.extend(items)

    synthesizer = IntelSynthesizer()
    categorized = synthesizer.synthesize(all_items, top_k_per_category=3)

    # 1. Publish Markdown
    md_pub = MarkdownPublisher()
    md_content = md_pub.format_digest(categorized)
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"[+] Successfully generated Markdown briefing: {output_md}")

    # 2. Publish HTML Email
    html_pub = EmailHTMLPublisher()
    html_content = html_pub.format_html(categorized)
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[+] Successfully generated HTML Email briefing: {output_html}")

def main():
    parser = argparse.ArgumentParser(description="Intel-Pulse: Autonomous AI & Deep-Tech Intelligence Engine")
    parser.add_argument("--config", default="config/feeds.json", help="Path to feeds JSON config")
    parser.add_argument("--out-md", default="LATEST_DIGEST.md", help="Output path for Markdown briefing")
    parser.add_argument("--out-html", default="LATEST_DIGEST.html", help="Output path for HTML briefing")
    args = parser.parse_args()

    run_pipeline(config_path=args.config, output_md=args.out_md, output_html=args.out_html)

if __name__ == "__main__":
    main()
