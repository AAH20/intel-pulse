import unittest
from intel_pulse.fetcher import FeedItem
from intel_pulse.synthesizer import IntelSynthesizer
from intel_pulse.publisher import MarkdownPublisher, EmailHTMLPublisher

class TestIntelPulse(unittest.TestCase):
    def setUp(self):
        self.sample_items = [
            FeedItem(
                title="DeepSeek-V3 Inference Optimization on Apple Silicon",
                link="https://example.com/1",
                summary="Benchmarking 671B MoE inference using unified memory.",
                source_name="HackerNews",
                category="applied_engineering"
            ),
            FeedItem(
                title="DeepSeek-V3 Inference Optimization on Apple Silicon",  # Duplicate title
                link="https://example.com/2",
                summary="Duplicate summary.",
                source_name="ArXiv",
                category="applied_engineering"
            ),
            FeedItem(
                title="Bounded Model Checking for Distributed Agent Sagas",
                link="https://example.com/3",
                summary="Formal verification of two-phase commit rollbacks.",
                source_name="ArXiv",
                category="research_breakthroughs"
            )
        ]

    def test_deduplication(self):
        synthesizer = IntelSynthesizer()
        unique = synthesizer.deduplicate(self.sample_items)
        self.assertEqual(len(unique), 2)

    def test_markdown_and_html_generation(self):
        synthesizer = IntelSynthesizer()
        categorized = synthesizer.synthesize(self.sample_items)
        
        md_pub = MarkdownPublisher()
        md_out = md_pub.format_digest(categorized)
        self.assertIn("INTEL-PULSE DAILY EXECUTIVE BRIEFING", md_out)
        self.assertIn("Bounded Model Checking", md_out)
        self.assertIn("a2zsoc.com", md_out)

        html_pub = EmailHTMLPublisher()
        html_out = html_pub.format_html(categorized)
        self.assertIn("<!DOCTYPE html>", html_out)
        self.assertIn("DeepSeek-V3", html_out)

if __name__ == "__main__":
    unittest.main()
