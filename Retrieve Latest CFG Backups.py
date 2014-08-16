import os
import shutil

pathpart = r'Q:\InternetMonitoringService\Configuration Files\prdidol'
here = os.getcwd()

for s in range(1,10):
	for f in (0,1,2):
		curdir = '{}S{}F{}'.format(pathpart,s,f)
		print(curdir)
		os.chdir(curdir)
		latest = max(os.listdir(curdir), key=lambda x: os.stat(x).st_mtime)
		print('Copying', latest, '...')
		shutil.copy2(latest, here)