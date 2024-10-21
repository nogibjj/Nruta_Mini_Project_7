import argparse
from mylib import query


def main():
    parser = argparse.ArgumentParser(description="Biopics Database Management CLI")
    parser.add_argument("--year", type=int, help="Filter biopics by release year")
    args = parser.parse_args()

    if args.year:
        # Example functionality: query the database for a specific year
        result = query.filter_by_year(args.year)
        print(result)
    else:
        print("Please specify a valid year.")


if __name__ == "__main__":
    main()
