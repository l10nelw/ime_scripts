"""
Converts config files to the new format
How to use: Drag config files on to this script file
Last modified: 2013-09-02
"""
import configparser
import ime
import os
import shutil
import sys

ADD_TO_DEFAULT = '''[{}]
ImportMustHaveCheck=65
FixedFieldName0=Author
FixedFieldName1=SourceRank
FixedFieldName2=Spiderjob
FixedFieldName3=SOURCENAME
FixedFieldName4=LOCATION
FixedFieldName5=keywords
FixedFieldName6=LANGUAGE
FixedFieldName7=SOURCETYPE
FixedFieldValue0=None
FixedFieldValue1=1
'''
NEW_KEYS_EACH_SPIJOB = ime.CfgPiece({
# new key: old key's value
'FixedFieldValue2': 'Directory',
'FixedFieldValue3': 'FixedFieldValue4',
'FixedFieldValue4': 'FixedFieldValue2',
'FixedFieldValue5': 'FixedFieldValue1',
'FixedFieldValue6': 'FixedFieldValue0',
'FixedFieldValue7': 'FixedFieldValue3',
})
NEW_KEYS_EACH_SPIJOB = sorted(NEW_KEYS_EACH_SPIJOB.items())

def end(e):
    input('Press Enter to continue')
    sys.exit(e)
    
def add_to_default(file):
	"add config from ADD_TO_DEFAULT"
    i = ime.index('DEFAULT', file.sections()) # get exact name of default section to account for all case combos (Default, DEFAULT, etc.)
    if i is not None: # if default section found
        file.read_string( ADD_TO_DEFAULT.format( file.sections()[i] ) )
    return file

def convert_sections(file):
	"make changes to each spiderjob"
    for sectionname in file:
        if sectionname.upper() in ime.NON_SPIDERJOBS: continue
        
        if 'FixedFieldValue1' not in file[sectionname]:
            print(sectionname, 'not converted: FixedFieldValue1 not found (spiderjob already converted or not a spiderjob)')
            continue
            
        # get new keys' values
        newkeys = ime.CfgPiece(NEW_KEYS_EACH_SPIJOB)
        for key in newkeys:
            newkeys[key] = file[sectionname][newkeys[key]]
        newkeys['FixedFieldValue2'] = sectionname
        
        # take unchanged parts of spiderjob
        top = ime.slice_cfg(file[sectionname], end='FixedFieldName0', end_inc=False, skip=('ImportMustHaveCheck', '//LOGFILE'))
        bot = ime.slice_cfg(file[sectionname], start='FixedFieldValue6', start_inc=False)
        
        # combine all parts
        file[sectionname] = top
        file[sectionname].update(newkeys)
        file[sectionname].update(bot)

    return file

def make_backup_file(filename):
    newfilename = filename
    while True:
        newfilename = os.path.splitext(newfilename)
        newfilename = newfilename[0] + ' (old)' + newfilename[1]
        if not os.path.exists(newfilename): break
    shutil.copy(filename, newfilename)
    return newfilename

def convert_file(filename):
    file = ime.CfgFile(keys_case_sensitive=True)

    # read
    try: file.read(filename)
    except (configparser.DuplicateSectionError, configparser.DuplicateOptionError) as e:
        e = str(e).split(']: ')
        e = e[0] + ']:\n' + e[1]
        print(e, '\nRemove the duplicate and try again.')
        end(1)

    # convert
    file = add_to_default(file)
    file = convert_sections(file)

    # backup
    backupfilename = make_backup_file(filename)
    
    # output
    with open(filename, 'w') as f:
        file.write(f, space_around_delimiters=False)
        print(filename, 'converted')
        print(backupfilename, 'created')

def main():
    filenames = ime.get_input_file()
    for filename in filenames: convert_file(filename)
    end(0)
    
if __name__=='__main__': main()
