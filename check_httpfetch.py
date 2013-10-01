# check for access to httpfetch.cfg in all spiders

import os

FILES = [r'\\prdidolspider{}\httpfetch$\HttpFetch_0\httpfetch.cfg'.format(spider) for spider in range(1, 14+1)]

for file in FILES:
	print(file, ':', os.path.exists(file))

input('Done. Press Enter to exit.')

