#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT
# Author: Andreas Lindhé

from docopt import docopt
from typing import List, Dict
from pathlib import Path
import os
import re
import sys

__version__ = "1.2.0"

docs = f"""
Fixes problems mostly caused by Apple.

Prints a list of `mv` commands that fixes the found issues.

USAGE:
  {sys.argv[0]} PATH [options]

ARGS:
  PATH              the path to check files in

OPTIONS:
  -h --help         print this help and exit
  -v --verbose      print more
  --version         print version and exit

"""

# characters_to_fix is a LUT from bad substring to good substring
# Really hard to visually inspect,
# but I promise the key is not what it looks like.
# Here's a good website to inspect them: <https://babelstone.co.uk/Unicode/whatisit.html>
characters_to_fix = {
    'å': 'å',
    'ä': 'ä',
    'ö': 'ö',
    'Å': 'Å',
    'Ä': 'Ä',
    'Ö': 'Ö'
    }


def main(path, verbose=False):
    """ Takes a path and checks the filenames for issues. """
    # This stolen from here: https://stackoverflow.com/a/3207973/893211
    original_filenames = []
    for (_, _, filenames) in os.walk(path):
        original_filenames.extend(filenames)
        break
    original_files = [str(Path(path).joinpath(f)) for f in original_filenames]
    bad_filenames = findProblems(strings=original_files)
    fixes = findFixes(bad_filenames)
    check_for_collisions(original_files, fixes.values())
    if verbose:
        print("Original filenames: " + str(original_files))
        print("Bad filenames: " + str(bad_filenames))
        print("Fixed filenames: " + str(fixes.values()))
    for fix in fixes:
        print("mv -i '" + fix + "' '" + fixes[fix] + "'")


def findFixes(broken_strings: List[str]) -> Dict[str, str]:
    fixes = {}
    for string in broken_strings:
        fixes[string] = fixProblem(string)
    return fixes


def check_for_collisions(a: List[str], b: List[str],
                         warning="WARNING! Collision found!"):
    """ If elements in lists a and b are similar, print a warning and exit """
    collision = set(a) & set(b)
    if collision:
        sys.exit(warning + "\n\n" + str(collision))


def findProblems(strings: List[str]) -> List[str]:
    bad_strings: List[str] = []
    for bad_char in characters_to_fix:
        bad_strings = bad_strings + [s for s in strings if bad_char in s]
    return bad_strings


def fixProblem(bad_string: str) -> str:
    """ Takes a bad string and fixes it """
    for bad_char in characters_to_fix:
        bad_string = re.sub(
            pattern=bad_char,
            repl=characters_to_fix[bad_char],
            string=bad_string)
    return bad_string


if __name__ == '__main__':
    args = docopt(docs, version=__version__)
    try:
        main(path=args['PATH'], verbose=args['--verbose'])
    except KeyboardInterrupt:
        sys.exit("\nInterrupted by ^C\n")
