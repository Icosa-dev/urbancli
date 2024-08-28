from typing import List

# escape codes
BLACK = '\x1b[30m'
RED = '\x1b[31m'
GREEN = '\x1b[32m'
YELLOW = '\x1b[33m'
BLUE = '\x1b[34m'
MAGENTA = '\x1b[35m'
CYAN = '\x1b[36m'
WHITE = '\x1b[37m'

BG_BLACK = '\x1b[40m'
BG_RED = '\x1b[41m'
BG_GREEN = '\x1b[42m'
BG_YELLOW = '\x1b[43m'
BG_BLUE = '\x1b[44m'
BG_MAGENTA = '\x1b[45m'
BG_CYAN = '\x1b[46m'
BG_WHITE = '\x1b[47m'

RESET = '\x1b[0m'
BOLD = '\x1b[1m'
DIM = '\x1b[2m'
UNDERLINED = '\x1b[4m'
BLINKING = '\x1b[5m'
REVERSE_VIDEO = '\x1b[7m'
HIDDEN = '\x1b[8m'

def stylize(text: str, escape_codes: List[str]) -> str:
    return f"{''.join(escape_codes)}{text}{RESET}"