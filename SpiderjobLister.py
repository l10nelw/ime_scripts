"""
Lists spiderjobs in a config file
How to use: Drag a config file on to this script file
"""

import ime
import os

def process_and_output(cfg):
    outfile = 'SpiderjobList.txt'
    joblist = [job for job in cfg if job.upper() not in ime.NON_SPIDERJOBS]
    with open(ime.addpath(outfile), 'w') as f:
        for job in joblist:
            f.write(job + '\n')
            print(job)
        print()
        print('Output to', outfile)

def main():
    run = True
    pathname = ime.get_input_file()[0]

    if os.path.isfile(pathname):
    
        cfg = ime.CfgFile()
        
        try:
            cfg.read(pathname)
        except:
            print('Error opening file')
            run = False
            
        if run: process_and_output(cfg)
        
    else:
        print('File not found')
        
    input('Press Enter to exit')
    
if __name__=='__main__': main()

