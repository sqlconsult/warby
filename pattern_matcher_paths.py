import re

class PatternMatcher():
    def __init__(self, user_patterns, module_logger):
        """
        Class constructor
        :param user_patterns    Dictionary of user patterns
        :param module_logger    Logging module

        Sample user_patterns:
            {'num_wildcards': 0, 'pattern_regex': 'foo/bar/baz', 'pattern_len': 3, 'input_pattern': 'foo,bar,baz'}, 
            {'num_wildcards': 2, 'pattern_regex': '^./b/.', 'pattern_len': 3, 'input_pattern': '*,b,*'}, 
            {'num_wildcards': 2, 'pattern_regex': 'a/./.', 'pattern_len': 3, 'input_pattern': 'a,*,*'}, 
            {'num_wildcards': 2, 'pattern_regex': '^././c', 'pattern_len': 3, 'input_pattern': '*,*,c'}, 
            {'num_wildcards': 1, 'pattern_regex': '^./x/y/z', 'pattern_len': 4, 'input_pattern': '*,x,y,z'}, 
            {'num_wildcards': 2, 'pattern_regex': 'w/x/./.', 'pattern_len': 4, 'input_pattern': 'w,x,*,*'}
        """
        self.module_logger = module_logger
        self.user_patterns = user_patterns

    def run(self, path_to_check):
        """
        Main entry point to compare

        :param path_to_check    Path under consideration dictionary
                                    'input_path': string - original input path,
                                    'clean_path': string - path with leading and trailing
                                                           slashs removed,
                                    'path_len':   integer - number of elements in this path

        path_to_check examples:
            {'input_path': 'foo/', 'path_len': 1, 'clean_path': 'foo'}, 
            {'input_path': 'foo/bar/', 'path_len': 2, 'clean_path': 'foo/bar'}, 
            {'input_path': 'a/b/c', 'path_len': 3, 'clean_path': 'a/b/c'}, 
            {'input_path': 'foo/bar/baz/', 'path_len': 3, 'clean_path': 'foo/bar/baz'}, 
            {'input_path': '/w/x/y/z/', 'path_len': 4, 'clean_path': 'w/x/y/z'}]
        """

        # initialize
        match_flag = False              # not matched
        num_wildcards_in_match = 99999  # some very big number of wildcards
        match_pattern = None            # 'best' pattern match to this path

        # loop over patterns.  already sorted by original pattern
        for i in range(len(self.user_patterns['patterns'])):
            pattern = self.user_patterns['patterns'][i]
            # if this pattern different num elements than the path, check next pattern
            if pattern['pattern_len'] != path_to_check['path_len']:
                continue

            # compare path to regex pattern
            regex_pattern = pattern['pattern_regex']                
            matched = re.match(regex_pattern, path_to_check['clean_path'])

            # if a match, append pattern and stop checking
            if matched:
                match_flag = True
                if pattern['num_wildcards'] < num_wildcards_in_match:
                    match_pattern = pattern['input_pattern']
                    num_wildcards_in_match = pattern['num_wildcards']

        if match_flag:
            return match_pattern
        else:
            return 'NO MATCH'
