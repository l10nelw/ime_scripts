#checks for the latest modified file in the listed locations

import os
import glob
import datetime

SERVER_PATHS_LIST = [r'\\prdidolspider{}\urlfiles$\*'.format(s) for s in range(1, 11+1)]

today = datetime.date.today().isoformat()

def getdatemodified(file):
	return datetime.datetime.fromtimestamp(os.stat(file).st_mtime).date().isoformat()

def latestfiledate(server_path):
	files = glob.iglob(server_path)
	latest = ''
	for file in files:
		date = getdatemodified(file)
		latest = date if date > latest else latest
		if date == today: break
	print('Latest:', latest)

# main #
for server_path in SERVER_PATHS_LIST:
	print('Checking', server_path, end='... ')
	latestfiledate(server_path)

input('Done. Press Enter to exit.')
