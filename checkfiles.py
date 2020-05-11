#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT
# Author: Andreas Lindhé

from docopt import docopt
from typing import List
import os
import re
import sys

__version__ = "0.1.0"

docs = f"""
Fixes problems mostly caused by Apple.

USAGE:
  {sys.argv[0]} PATH [--help] [--version]

ARGS:
  PATH              the path to check files in

OPTIONS:
  -h --help         print this help and exit
  --version         print version and exit

"""

# fix is a LUT from bad substring to good substring
# Really hard to visually inspect,
# but I promise the key is not what it looks like.
fix = {
    'ä': 'ä',
    'ö': 'ö'
    }

def main(path = '.'):
  """ Takes a path and checks the filenames for issues. """
  original_filenames = os.listdir(path = path)
  bad_filenames = findProblems(files = original_filenames)
  fixed_filenames = [fixProblem(f) for f in bad_filenames]
  check_for_collisions(original_filenames, fixed_filenames)
  pass

def check_for_collisions(a: List[str], b: List[str], warning = "WARNING! Collision found!"):
  """ If elements in lists a and b are similar, print a warning and exit """
  collision = set(a) & set(b)
  if collision:
    sys.exit(warning + "\n\n" + str(collision))

def promptForReplacement(files_to_replace: List[str]):
  """ Prompts the user to rename files """
  pass

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
    main(path = args['PATH'])
  except KeyboardInterrupt:
    sys.exit("\nInterrupted by ^C\n")
