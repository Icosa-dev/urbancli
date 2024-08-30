import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="urban", description="A command line interface for Urban Dictionary")

    parser.add_argument("word", type=str, help="The word to search up (default: \"python\")")
    parser.add_argument("-x", "--extra-entries", type=int, help="Number of extra entries to show (default: 0)")
    parser.add_argument("-e", "--entry", type=int, help="Entry number of the definition to show (default: 1)")

    return parser.parse_args()
