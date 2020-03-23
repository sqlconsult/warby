# Pattern-Matching Paths

> Solution for Pattern-Matching Paths coding challenge.

> This solution reads the user input patterns and paths from STDIN and 
> prints either the 'best' matching pattern or 'NO MATCH' to STDOUT.

## Solution Files

1. controller.py
-     Main entry point
      Sample execution command: cat user_inputs.txt | python controller.py
2. logger.py
-     Logging module
3. pattern_matcher_paths.py
-     Matches paths to patterns: Uses patterns that were converted to regex expressions
      and compares to path under consideration.  Return 'best' match or 'NO MATCH' for
      each path.
4.  read_inputs.py
-     Reads patterns and paths: Patterns are mapped to regex expressions and paths are cleaned
      of leadint and trailing slashes ('/')
5.  SoftwareEngineer.md
-     Coding challenge statement & requirements
6.  user_inputs.txt
-     Test input file