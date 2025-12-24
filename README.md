
# Pulse Coding Assignment – SaaS Review Scraper

## Overview
This project scrapes SaaS product reviews from **G2**, **Capterra**, and an optional **third source (TrustRadius)**.
It accepts company name, date range, and source as inputs and outputs reviews in structured JSON format.

## Features
- Supports G2, Capterra, TrustRadius
- Date range filtering
- Pagination handling
- Graceful error handling
- Clean, modular Python code

## Requirements
- Python 3.9+
- requests
- beautifulsoup4
- dateparser

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py --company "Slack" --source g2 --start_date 2024-01-01 --end_date 2024-06-30
```

## Output
JSON file saved in `output/` directory.

## Notes
- Scraping respects pagination and basic rate limiting.
- Some platforms may require headers/user-agent rotation.
- Some selectors may need adjustment as platforms update UI
- Future work: async scraping, proxy rotation
