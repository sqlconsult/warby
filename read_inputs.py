import sys

from pattern_matcher_paths import PatternMatcher


class ReadInputs():
    """
    Class to read and process user inputs
    """
    def __init__(self, module_logger):
        """
        Constructor

        :param user_patterns   Dictionary of user patterns
        :param module_lgger    Logging module object
                'num_patterns': integer
                'patterns':     pattern dictionary
                                    'input_pattern': string - original input pattern
                                    'pattern_regex': string - pattern mapped to regex string
                                    'pattern_len':   integer - number of elements in patterh
                                    'num_wildcards': integer - number of wildcards in pattern
        """
        self.user_patterns = {'num_patterns': 0, 'patterns': None}
        self.module_logger = module_logger


    def read_patterns(self):
        """
        Read STDIN to get patterns

        Return:   Pattern dictionary
                      'num_patterns': integer
                      'patterns':     pattern dictionary
                                          'input_pattern': string,
                                          'pattern_regex': string,
                                          'pattern_len':   integer,
                                          'num_wildcards': integer
        """
        #
        # There are 12 characters with special meanings: 
        #    backslash \, 
        #    caret ^, 
        #    dollar sign $, 
        #    period or dot ., 
        #    vertical bar or pipe symbol |, 
        #    question mark ?, 
        #    asterisk or star *, 
        #    plus sign +, 
        #    opening parenthesis (, 
        #    closing parenthesis ), 
        #    opening square bracket [, 
        #    opening curly brace {
        #    These special characters are often called “metacharacters”. 
        #    Most of them are errors when used alone.
        #
                
        # 1st input is number of patterns
        self.user_patterns['num_patterns'] = int(input())

        # invalid input, can't proceed
        if self.user_patterns['num_patterns'] == 0:
            print('ERROR: Number of patterns to use is zero')
            sys.exit(1)

        # read patterns 1 at a time all_patterns
        all_patterns = []
        for _ in range(self.user_patterns['num_patterns']):
            input_pattern = input()
            #
            # convert pattern to regex expression
            #
            # commas become slash
            pattern_regex = input_pattern.replace(',', '\\/')

            # '*' becomes '.' to match any single character
            pattern_regex = pattern_regex.replace('*', '.*')

            # if pattern starts with wildcard (now a '.')
            # insert '^' - regex starts with
            if pattern_regex[0] == '.':
                pattern_regex = '^' + pattern_regex

            # if pattern ends with wildcard (now a '.')
            # insert '$' - regex ends with
            if pattern_regex[-2:] == '.*':
                pattern_regex = pattern_regex + '$'

            # get # of elements in pattern
            pattern_len = len(input_pattern.split(','))

            # count the number of wildcards inn the pattern
            num_wildcards = input_pattern.count('*')

            pattern_dict = {
                'input_pattern': input_pattern,
                'pattern_regex': pattern_regex,
                'pattern_len': pattern_len,
                'num_wildcards': num_wildcards}

            all_patterns.append(pattern_dict)

        # sort so letters come before wildcards
        sorted_patterns = sorted(all_patterns, \
            key=lambda k: k['input_pattern'], reverse=True)

        self.user_patterns['patterns'] = sorted_patterns

        return None


    def process_paths(self):
        """
        Read STDIN to get paths 1 at a time and compare against user_patterns

        Return: List of pattern matches or 'NO MATCH'
        """
        # initialize return list
        ret_val = []

        # read number of paths to check
        num_paths = int(input())

        # invalid input, can't proceed
        if num_paths == 0:
            print('ERROR: Number of paths to check is zero')
            sys.exit(1)

        # instantiate pattern_matcher object
        pattern_matcher_obj = PatternMatcher(self.user_patterns, self.module_logger)

        for _ in range(num_paths):
            # get each input path
            input_path = input()

            # remove leading and trailing '/'
            clean_path = input_path
            if clean_path[0] == '/':
                clean_path = clean_path[1:]

            if clean_path[-1] == '/':
                clean_path = clean_path[:-1]

            # get # of elements in path
            path_len = len(clean_path.split('/'))

            path_dict = {
                'input_path': input_path,
                'clean_path': clean_path,
                'path_len': path_len}

            result = pattern_matcher_obj.run(path_dict)

            ret_val.append(result)

        return ret_val
