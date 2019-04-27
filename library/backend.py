import os
import configparser

# TEMP TESTING ONLY
dir = r"F:\My Games\Bethesda Modding\SkyrimSE\mods"

def get_mods(dir):
    mods = {}

    with os.scandir(dir) as mod_dir:
        # Checks for all mod folders
        mod_folders = [directory for directory in mod_dir if (directory.is_dir())]
        config = configparser.ConfigParser()

        # Checks for meta.ini in each folder
        for mod in mod_folders:
            path = mod.path
            # If the mod folder is actually a Mod Organizer separator, ignore it
            if mod.name.endswith('separator'):
                continue

            # Default Values
            url = ''
            id = 0

            # Open config with configparser
            try:
                config.read(f'{path}\\meta.ini')
                url = config['General']['url']
            except Exception as e: #Generic I know
                if e == 'url':
                    print(f'Warning: Mod "{mod.name}" has no url')
                else:
                    print('Warning: Encountered Exception: {} for {}'.format(e, mod.name))

            # Checks for valid Nexus url (cdn urls break)
            if not check_url(url):
                print(f'WARNING: Mod "{mod.name}" does not have a valid Nexus URL')
                url = '' #Overwrite the bad URL so we can search Nexus for it later

            mods[mod.name] = {
                'url':url,
                'path':mod.path,
             }
            # DEBUG: print(url)
    return mods

def check_url(url):
    if url.find('nexusmods.com') != -1:
        return True
    else:
        return False

# Leaves url ending with /
def strip_url(url):
    if url.endswith('/'):
        return url
    else:
        end = url.rfind('/')
        return url[:end+1]

def test_functions():
    print('Testing get_mods:')
    mods = get_mods(dir)
    print(str(mods)+'\n')


# test_functions()
