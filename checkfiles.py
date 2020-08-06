#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT
# Author: Andreas Lindhé

from docopt import docopt
from typing import List, Dict
import os
import re
import sys

__version__ = "0.1.0"

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

# fix is a LUT from bad substring to good substring
# Really hard to visually inspect,
# but I promise the key is not what it looks like.
fix = {
    'ä': 'ä',
    'ö': 'ö'
    }


def main(path, verbose=False):
    """ Takes a path and checks the filenames for issues. """
    # This stolen from here: https://stackoverflow.com/a/3207973/893211
    original_filenames = []
    for (_, _, filenames) in os.walk(path):
        original_filenames.extend(filenames)
        break
    bad_filenames = findProblems(strings=original_filenames)
    fixes = findFixes(bad_filenames)
    check_for_collisions(original_filenames, fixes.values())
    if verbose:
        print("Original filenames: " + str(original_filenames))
        print("Bad filenames: " + str(bad_filenames))
        print("Fixed filenames: " + str(fixes.values()))
    for fix in fixes:
        print("mv " + fix + " " + fixes[fix])


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
    for shit in fix:
        bad_strings = bad_strings + [s for s in strings if shit in s]
    return bad_strings


def fixProblem(bad_string: str) -> str:
    """ Takes a bad string and fixes it """
    for shit in fix:
        bad_string = re.sub(pattern=shit, repl=fix[shit], string=bad_string)
    return bad_string


if __name__ == '__main__':
    args = docopt(docs, version=__version__)
    try:
        main(path=args['PATH'], verbose=args['--verbose'])
    except KeyboardInterrupt:
        sys.exit("\nInterrupted by ^C\n")
