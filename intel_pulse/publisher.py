import datetime
from typing import Dict, List
from .fetcher import FeedItem

class MarkdownPublisher:
    """Formats executive intelligence digest as clean GitHub-flavored Markdown."""
    def format_digest(self, categorized_items: Dict[str, List[FeedItem]]) -> str:
        date_str = datetime.datetime.now(datetime.timezone.utc).strftime("%B %d, %Y")
        
        md = f"# ⚡ INTEL-PULSE DAILY EXECUTIVE BRIEFING\n\n"
        md += f"**Date:** {date_str} | **Curator:** Ahmed Hassan ([A2Z SOC](https://a2zsoc.com))\n\n"
        md += f"---\n\n"

        category_labels = {
            "research_breakthroughs": "🔬 RESEARCH BREAKTHROUGHS & ALGORITHMIC ADVANCES",
            "applied_engineering": "⚙️ APPLIED SYSTEMS & PRODUCTION ENGINEERING",
            "industry_trends": "📈 INDUSTRY DISPATCHES & HIGHLIGHTS",
            "macro_intelligence": "🌐 MACRO INTELLIGENCE & GOVERNANCE",
        }

        for cat_key, items in categorized_items.items():
            label = category_labels.get(cat_key, cat_key.upper().replace("_", " "))
            md += f"### {label}\n\n"
            for item in items:
                md += f"* **[{item.title}]({item.link})** — *{item.source_name}*\n"
                if item.summary:
                    md += f"  > {item.summary}\n"
                md += "\n"

        md += "---\n\n"
        md += "### 💡 ARCHITECT'S TAKEAWAY & MONETIZATION LEVERAGE\n"
        md += "To build enduring leverage in 2026, engineering teams must move beyond passive tracking and anchor directly into autonomous execution planes. Explore enterprise governance and autonomous SOC architectures at **[a2zsoc.com](https://a2zsoc.com)**.\n"

        return md

class EmailHTMLPublisher:
    """Formats executive intelligence digest into responsive HTML email for Ghost, Beehiiv, or Listmonk."""
    def format_html(self, categorized_items: Dict[str, List[FeedItem]]) -> str:
        date_str = datetime.datetime.now(datetime.timezone.utc).strftime("%B %d, %Y")
        html_out = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset="utf-8">
          <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #1a1a1a; max-width: 650px; margin: 0 auto; padding: 20px; }}
            h1 {{ color: #0f172a; font-size: 24px; border-bottom: 2px solid #0284c7; padding-bottom: 8px; }}
            h2 {{ color: #0284c7; font-size: 18px; margin-top: 24px; }}
            .item {{ margin-bottom: 16px; }}
            .item a {{ color: #0369a1; font-weight: 600; text-decoration: none; }}
            .item a:hover {{ text-decoration: underline; }}
            .meta {{ font-size: 12px; color: #64748b; }}
            .summary {{ font-size: 14px; color: #334155; margin: 4px 0 0 0; }}
            .footer {{ margin-top: 32px; padding-top: 16px; border-top: 1px solid #e2e8f0; font-size: 13px; color: #64748b; }}
          </style>
        </head>
        <body>
          <h1>⚡ Intel-Pulse Executive Briefing</h1>
          <p><strong>{date_str}</strong> | Curated by <a href="https://a2zsoc.com">A2Z SOC</a></p>
        """

        category_labels = {
            "research_breakthroughs": "🔬 Research Breakthroughs",
            "applied_engineering": "⚙️ Applied Systems & Engineering",
            "industry_trends": "📈 Industry Highlights",
            "macro_intelligence": "🌐 Macro Intelligence",
        }

        for cat_key, items in categorized_items.items():
            label = category_labels.get(cat_key, cat_key.upper().replace("_", " "))
            html_out += f"<h2>{label}</h2>"
            for item in items:
                html_out += f"""
                <div class="item">
                  <a href="{item.link}" target="_blank">{item.title}</a> <span class="meta">({item.source_name})</span>
                  <p class="summary">{item.summary}</p>
                </div>
                """

        html_out += """
          <div class="footer">
            <p><strong>A2Z SOC Intelligence:</strong> Real-time sovereign AI governance and continuous compliance. Visit <a href="https://a2zsoc.com">a2zsoc.com</a>.</p>
          </div>
        </body>
        </html>
        """
        return html_out
