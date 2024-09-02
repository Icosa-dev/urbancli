# Urban CLI

`urbancli` is a command line interface tool that allows you to access the urban dictionary from the command line.

## Install

To install urbancli you need to clone the git repository and run the `install.sh` script. This will copy the needed files into `~/.local/bin`. You will need to add `~/.local/bin` to your PATH if it is not already there for it to work properly.

```
git clone https://gitlab.com/Icosaa/urbancli
cd urbancli

chmod +x install.sh
./install.sh
# you can run ./install.sh uninstall to remove urbancli 
```

## Usage

```
usage: urban [-h] [-x EXTRA_ENTRIES] [-e ENTRY] [word]

A command line interface for Urban Dictionary

positional arguments:
  word                  The word to search up (default: "python")

options:
  -h, --help            show this help message and exit
  -x EXTRA_ENTRIES, --extra-entries EXTRA_ENTRIES
                        Number of extra entries to show (default: 0)
  -e ENTRY, --entry ENTRY
                        Entry number of the definition to show (default: 1)
```