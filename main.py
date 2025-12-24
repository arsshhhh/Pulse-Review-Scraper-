
import argparse
from scrapers.g2 import scrape_g2
from scrapers.capterra import scrape_capterra
from scrapers.trustradius import scrape_trustradius
from utils.io import save_json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--company", required=True)
    parser.add_argument("--source", required=True, choices=["g2", "capterra", "trustradius"])
    parser.add_argument("--start_date", required=True)
    parser.add_argument("--end_date", required=True)
    args = parser.parse_args()

    if args.source == "g2":
        reviews = scrape_g2(args.company, args.start_date, args.end_date)
    elif args.source == "capterra":
        reviews = scrape_capterra(args.company, args.start_date, args.end_date)
    else:
        reviews = scrape_trustradius(args.company, args.start_date, args.end_date)

    save_json(reviews, args.company, args.source)

if __name__ == "__main__":
    main()
