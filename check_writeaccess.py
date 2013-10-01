# check for write access to folders in all spiders

import os

SPIDERS = range(1, 14+1)
FOLDERS = 'idolserver', 'httpfetch', 'urlfilefilter', 'urlfiles'
PATH_FORMAT = r'\\prdidolspider{spider}\{folder}$'

for spider in SPIDERS:
    for folder in FOLDERS:
        path = PATH_FORMAT.format(spider=spider, folder=folder)
        print(path, '\t\t', os.access(path, os.W_OK))

input('Done. Press Enter to exit.')

