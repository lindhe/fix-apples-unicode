#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT
# Author: Andreas Lindhé

from typing import List
import os
import re
import sys


# fix is a LUT from bad substring to good substring
# Really hard to visually inspect,
# but I promise the key is not what it looks like.
fix = {
    'ä': 'ä',
    'ö': 'ö'
    }

def main(path = '.'):
  """ Takes a path and checks the filenames for issues. """
  all_files = os.listdir(path = path)
  bad_files = findProblems(files = all_files)
  promptForReplacement(files_to_replace = bad_files)
  pass

def promptForReplacement(files_to_replace: List[str]):
  pass

def findProblems(strings: List[str]) -> List[str]:
  bad_strings: List[str] = []
  for shit in fix:
    bad_strings = bad_strings + [s for s in strings if shit in s]
  return bad_strings


def fixString(bad_string: str) -> str:
  """ Takes a bad string and fixes it """
  for shit in fix:
      bad_string = re.sub(pattern=shit, repl=fix[shit], string=bad_string)
  return bad_string


if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    sys.exit("\nInterrupted by ^C\n")
