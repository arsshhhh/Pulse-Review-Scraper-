
# Bonus: Third Review Source Integration (TrustRadius)

## Overview
In addition to G2 and Capterra, this project integrates **TrustRadius** as a third SaaS review source
to earn bonus points as specified in the assignment.

TrustRadius is a well-known B2B software review platform that provides detailed, high-quality
user reviews, ratings, and reviewer context.

---

## Supported Sources
The script currently supports the following sources:

1. **G2**
2. **Capterra**
3. **TrustRadius (Bonus Source)**

All sources follow the same interface and output format.

---

## How TrustRadius Integration Works

### 1. URL Resolution
The scraper dynamically constructs the TrustRadius review URL using the company name:

```
https://www.trustradius.com/products/<company-name>/reviews
```

Example:
```
https://www.trustradius.com/products/slack/reviews
```

Company names are normalized (lowercased, spaces replaced with hyphens).

---

### 2. Scraping Logic
- Uses `requests` with a browser-like User-Agent
- Parses HTML using `BeautifulSoup`
- Extracts:
  - Review title
  - Review text
  - Review date
  - Rating (if available)
- Dates are normalized using `dateparser`
- Reviews outside the provided date range are ignored

---

### 3. Unified Output Format
TrustRadius reviews are returned in the **same JSON schema** as G2 and Capterra:

```json
{
  "title": "Great collaboration tool",
  "review": "Slack improved our internal communication significantly.",
  "date": "2024-03-18",
  "rating": "9/10"
}
```

This ensures downstream systems can consume reviews without source-specific handling.

---

## How to Use the Third Source

### Command
```bash
python main.py --company "Slack" --source trustradius --start_date 2024-01-01 --end_date 2024-06-30
```

### Output
A JSON file will be generated in the `output/` directory:
```
Slack_trustradius_<date>.json
```

---

## Error Handling & Limitations
- If TrustRadius changes page structure, selectors may need minor updates
- Rate limiting is respected via conservative request usage
- The scraper fails gracefully if no reviews are found

---

## Why TrustRadius Was Chosen
- B2B-focused SaaS reviews
- High-quality written feedback
- Complements G2 and Capterra well
- Commonly used by product and engineering teams

---

## Future Enhancements
- Add async scraping for faster execution
- Proxy rotation for higher-scale scraping
- Review sentiment scoring

