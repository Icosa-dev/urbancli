import math
from pyurbandict import UrbanDict
from typing import Callable
import dictdisplay.colors as colors

bold_blue = [colors.BLUE, colors.BOLD]
bold_blue_underlined = bold_blue + [colors.UNDERLINED]

def print_word(word: str, entry_num: int): 
    print(f"{colors.stylize(word + f" [{entry_num}]", bold_blue_underlined)}")

def print_definition(definition: str):
    print("\t" + definition + "\n")

def print_example(example: str):
    print(f"{colors.stylize('Example: ', bold_blue)}\n{example}\n")

def print_author(author: str):
    print(f"{colors.stylize('Author: ', bold_blue)}{author}")

def print_ratings(thumbs_up: int, thumbs_down: int):
    to_percent: Callable[[float], str] = lambda val: str(math.ceil(val * 100)) + "%"

    total_ratings = thumbs_up + thumbs_down
    approval_rating = thumbs_up / total_ratings
    disapproval_rating = thumbs_down / total_ratings

    print(f"{colors.stylize('Ratings: ', bold_blue)}", end="")  # end="" removes the extra newline
    if (approval_rating > disapproval_rating):
        print(f"👍: {thumbs_up} 👎: {thumbs_down} ({colors.stylize(to_percent(approval_rating), [colors.GREEN, colors.BOLD])})")
    else:
        print(f"👍: {thumbs_up} 👎: {thumbs_down} ({colors.stylize('-' + to_percent(disapproval_rating), [colors.RED, colors.BOLD])})")

# entries are 1 indexed
def print_entry(word: str, entry: int):
    results = UrbanDict(word).search()
    if results is not None:
        result = results[entry - 1]

        print_word(result.word, entry)
        print_definition(result.definition)
        print_example(result.example)
        print_author(result.author)
        print_ratings(result.thumbs_up, result.thumbs_down)
    else:
        print(f"{word} does not exist in the urban dictionary.");