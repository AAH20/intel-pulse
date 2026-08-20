# Intel-Pulse (`intel-pulse`)

**Autonomous High-Signal AI & Deep-Tech Intelligence Engine: Automated RSS/ArXiv Ingestion, Semantic Deduplication, Executive Synthesis & Multi-Channel Publisher.**

[![License](https://img.shields.io/badge/license-MIT%2FApache--2.0-blue.svg)](LICENSE)
[![Zero-Dependency](https://img.shields.io/badge/Dependencies-Standard%20Library%20(Pure%20Python)-brightgreen.svg)]()
[![Automated-Publishing](https://img.shields.io/badge/Schedule-Daily%2006%3A00%20UTC-orange.svg)]()

---

## 1. Overview

`Intel-Pulse` is an autonomous intelligence pipeline designed to capture industry attention, filter signal from noise across 50+ technical feeds (ArXiv, HackerNews, specialized engineering weblogs), and automatically generate executive markdown and HTML newsletters.

* **Zero-Dependency Standard Library Core:** Fast, resilient XML/Atom/RSS parser with automatic HTML sanitization.
* **Semantic Deduplication:** Eliminates cross-posted duplicate stories across aggregators.
* **Multi-Format Publisher:** Generates both GitHub-flavored Markdown briefings and responsive HTML emails ready for Ghost, Beehiiv, Substack, or Listmonk.
* **Autonomous Cron:** Runs daily via GitHub Actions at 06:00 UTC with zero server costs.

---

## 2. Quickstart

### Installation
```bash
pip install intel-pulse
```

### Run Locally
```bash
python3 -m intel_pulse.cli --config config/feeds.json --out-md LATEST_DIGEST.md --out-html LATEST_DIGEST.html
```

---

## 3. Architecture

```
intel-pulse/
├── config/
│   └── feeds.json         # Curated list of high-signal feeds (ArXiv, HN, Engineering blogs)
├── intel_pulse/
│   ├── __init__.py
│   ├── fetcher.py         # Resilient XML/Atom/RSS ingestor with custom User-Agent
│   ├── synthesizer.py     # Deduplication & category clustering engine
│   ├── publisher.py       # Markdown & HTML email template formatters
│   └── cli.py             # CLI runner
├── tests/
│   └── test_pipeline.py   # Verified unit test suite
└── .github/workflows/
    └── daily_publish.yml  # Automated daily publishing workflow
```

---

## 4. Audience & Monetization Leverage

`Intel-Pulse` acts as the top-of-funnel audience builder for **[A2Z SOC](https://a2zsoc.com)**, aggregating engineering leaders, VPs of Infrastructure, and AI founders around curated, high-signal technical breakthroughs.

---

## 5. Author

**Ahmed Hassan**  
*Principal AI Systems Architect | Founder, A2Z SOC*  
* LinkedIn: [Ahmed Hassan](https://eg.linkedin.com/in/ahmed-hassan-f11)  
* Platform: [A2Z SOC](https://a2zsoc.com)
