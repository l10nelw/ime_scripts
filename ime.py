"""
ime.py 2.3
modified: 2013-08-29

[section]
key/option=value

ime.NON_SPIDERJOBS
    List of names of config sections that are not spiderjobs, all in uppercase.
    
ime.CfgFile()
    Shorthand to initialise a config file variable. Config inside each section is in OrderedDict form.

ime.CfgPiece()
    Shorthand to initialise an OrderedDict variable.
    
ime.same()
	Checks if 2 strings are equal, case-insensitive.

ime.inside()
	Checks if string is in a list of strings, case-insensitive.

ime.index()
	Returns location of string in a list of strings, case-insensitive.

ime.slice_cfg()
    Slices a CfgPiece from start key to end key (both optional).
    
ime.addpath()
    Add path of the running script. Useful to ensure a file is located in the same place as the script.

ime.get_input_file()
    Get path names of files drag-and-dropped onto the running script, otherwise ask user for a path name.

ime.lf.data
ime.lf.list()
    A pre-initialised ListFilter object that can be fed a list of links (data) and a wildcard pattern in list() to filter it.

"""
import collections
import configparser
import fnmatch
import os
import sys

NON_SPIDERJOBS = ('', 'LICENSE', 'SERVICE', 'DEFAULT', 'SPIDER', 'LOGGING', 'ACTIONLOGSTREAM', 'APPLICATIONLOGSTREAM', 
                  'HTTPLOGSTREAM', 'INDEXLOGSTREAM', 'IMPORTLOGSTREAM', 'SPIDERLOGSTREAM')

def CfgFile(keys_case_sensitive=False):
    """
    CfgFile can store config, requires sections (appropriate for storing an entire cfg file)
    Delimiter is always '=', but lines without it are allowed; they become keys with no values
    Case-insensitive keys by default (recommended if only reading from file), can be set otherwise
    Create a CfgFile with: c = ime.CfgFile() or c = ime.CfgFile(keys_case_sensitive=True)
    """
    c = configparser.ConfigParser(delimiters=('='), default_section='', allow_no_value=True, interpolation=None)
    if keys_case_sensitive: c.optionxform = str
    return c

def CfgPiece(x=None):
    """
    CfgPiece can store a series of config lines without requiring a section
    Create a CfgPiece with: c = ime.CfgPiece()
    To get a detailed list of usable methods, type:
        import collections
        help(collections.OrderedDict)
    """
    return collections.OrderedDict(x) if x else collections.OrderedDict()

def same(a, b):
	"Check if 2 strings a and b are equal, case-insensitive"
	return a.upper() == b.upper()
	
def inside(needle, haystack):
	"Check if a string (needle) is in a list of strings (haystack), case-insensitive"
	return needle.upper() in (item.upper() for item in haystack) 

def index(needle, haystack):
    """
    Returns location of a string (needle) in a list of strings (haystack), case-insensitive.
    Location is a number from 0 (first) to the length of the list -1 (last), or None if not found.
    """
    for i, x in enumerate(haystack):
        if same(needle, x): return i
    return None

def slice_cfg(cfg, start='', start_inc=True, end='', end_inc=True, skip=()):
    """
    Slice a CfgPiece from start key to end key (both optional). Both are inclusive (start_inc and end_inc True) by default.
    
    e.g. slice_cfg(config, 'FixedFieldValue2', 'FixedFieldValue7')
         takes the portion of config from FixedFieldValue2 to FixedFieldValue7.
    
    e.g. slice_cfg(config, 'FixedFieldValue2', start_inc=False, FixedFieldValue7', end_inc=False)
         takes the portion of config from the line after FixedFieldValue2 to the line before FixedFieldValue7.
    
    Can supply optional list of keys to skip.
    
    e.g. slice_cfg(config, skip=('LogFile', 'ImportStripLinks', 'PageTimeout'))
         removes the LogFile, ImportStripLinks, and PageTimeout lines from config.
    
    Case-insenstive key checking.
    
    If start key not provided, starts at top. If end key not provided, ends at bottom. If both absent, cfg is not sliced.
    """
    cfgslice = CfgPiece()
    
    def add(cfg, key):
        cfgslice.update({ key: cfg[key] })
        
    go = True if start is '' else False
    
    for key in cfg:
        if same(key, start):
            if start_inc: add(cfg, key)
            go = True
            continue
        if same(key, end):
            if end_inc: add(cfg, key)
            break
        if inside(key, skip): continue
        if go: add(cfg, key)
        
    return cfgslice

def addpath(file=''):
    """
    Returns path of the running script
    If file given, returns path+file
    Useful to ensure a file is located in the same place as the script
    """
    path = os.path.split(os.path.realpath(__file__))[0]
    path += '\\' + file if file else ''
    return path

def get_input_file(prompt='Enter file name: '):
    "Get list of path names of files drag-and-dropped onto the running script, otherwise ask user for a path name"
    if len(sys.argv) > 1:
        return sys.argv[1:]
    else:
        return [input(prompt)]

class ListFilter:
    """
    A filtering tool that can be fed a list of links (data) and a wildcard pattern (filter) to filter the list
    Enter list in lf.data
    Display list with lf.list()
    Optionally enter list seperator in lf.sep (default is newline character)
    Filter and display list with lf.list(filter)
    
    e.g. >>> lf = ListFilter()
         >>> lf.data = '''
                http://website.com/news
                http://website.com/news/article1.html
                http://website.com/author/author1
                http://website.com/news/article2.html
                http://website.com/author/author2
                '''
         >>> lf.list('*.html')
         
         Result:
         http://website1.com/news/article1.html
         http://website1.com/news/article2.html
         2 out of 5
    """
    def __init__(self, data='', filter='*', sep='\n'):
        self.data = data
        self.sep = sep
        if data > '': self.list(filter)
    
    def unique(self, seq):
        "removes duplicates, preserving order"
        seen = set()
        seen_add = seen.add
        return [ x for x in seq if x not in seen and not seen_add(x) ]
    
    def list(self, filter='*'):
        """
        Set a wildcard pattern, execute filter and list results.
        If no pattern provided, lists the current data.
        """
        data = self.data.split(self.sep)
        data = self.unique(data)
        self.filtered = fnmatch.filter(data, filter)
        for item in self.filtered: print(item)
        print( '{} out of {}'.format(len(self.filtered), len(data)) )

lf = ListFilter()
# can type in IDLE: "from ime import lf"