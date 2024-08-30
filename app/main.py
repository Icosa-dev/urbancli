from pyurbandict import UrbanDict

import dictdisplay
import parser

def main():
    args = parser.parse_args()

    word = args.word
    entry = args.entry
    extra_entries = args.extra_entries

    total_entries = len(UrbanDict(word).search())

    if entry > total_entries:
        print(f"Urban: Error: entry {entry} does not exist for word \"{word}\"")
        return

    if extra_entries > total_entries:
        extra_entries = total_entries - 1

    while True:
        dictdisplay.print_entry(word, entry)

        extra_entries -= 1
        entry += 1

        if extra_entries <= 0:
            break

if __name__ == "__main__":
    main()
