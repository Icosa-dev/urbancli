import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="urban", description="A command line interface for Urban Dictionary")

    parser.add_argument("word", type=str, nargs='?', default="python", help='The word to search up (default: "python")')
    parser.add_argument("-x", "--extra-entries", type=int, default=0, help="Number of extra entries to show (default: 0)")
    parser.add_argument("-e", "--entry", type=int, default=1, help="Entry number of the definition to show (default: 1)")

    return parser.parse_args()