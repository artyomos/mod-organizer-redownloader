import os
import shutil
from library import backend
import webbrowser

# Main function - only called if opened
if __name__ == '__main__':
    print('Wecome to Nate\'s Mod Organizer Mod Redownloader!\n')
    while True:
        path = input('What is the path for the Mod Organizer MODS directory: ').strip()
        if os.path.isdir(path):
            break
        else:
            print('The path you gave was invalid! Make sure you are typing it properly...\n')

    mods = backend.get_mods(path)
    current = 0
    total = len(mods)

    print('\nFor each mod you have, you will be given the option to open the browser to the URL, or if the mod does not have a proper url, open the broswer to a Google Search for your mod. Some mods (Like a Bashed Patch) can be skipped by selecting the skip option out of the options provided for each mod.')
    print('\nFor your convienience, I have Included WARNING messages with a description of WHY. It is very likely that you will see a ton of warning messages indicating your mods do not have URLs, do not worry, we can search for them on Google :)')
    print('\nWARNING: It appears Mod Organizer is kinda dumb, so if you select go to download page and its for a COMPLETELY DIFFERENT MOD, it is NOT my fault! (I have encountered this myself several times, so included an optional checkup by the program, there is the option to search google in the case this happens, and I\'m sure google will help you out better)')
    print('(Pro Tip): Since we are talking about a lot of files and web pages, please note Ctrl+W closes a tab, and Alt+Tab switches back to this program :)')
    if len(mods) > 100:
        print('\nIt looks like we have a grand total of {} mods to redownload today! Wowza!'.format(len(mods)))
    input('Please Press enter to continue, if you are ready...')

    for mod in mods:
        current += 1
        print(f'\n**Working on mod "{mod}" ({current}/{total})**\n')
        url = mods[mod]['url']
        if url:
            # Remove extraneous info
            url = backend.strip_url(url)
            if input('What would you like to do?\n1 - Go to Nexus Page\tENTER - Skip Mod\n: ') == '1':
                print('Heading to Nexus. Make sure to choose the downloads you need!\n')
                webbrowser.open(url+'?tab=files')
            else: continue

            # A recheck to make sure it was good
            if input(f'Was your search for "{mod}" successful?\n1 - No, Google Search the Mod\tENTER - Just fine!\n: ') == '1':
                print('Heading to Google, make sure to get the right one for your game (SSE or Regular)!')
                query = mod.replace(' ','+')
                google = f'https://www.google.com/search?q={query}'
                webbrowser.open(google)
            else: continue
        else:
            if input('Uh Oh! Looks like this mod didn\'t have a valid file url! Your options are:\n1 - Do a Google Search for this mod\tENTER - Skip Mod\n: ') == '1':
                print('Heading to Google, make sure to get the right one for your game (SSE or Regular)!')
                query = mod.replace(' ','+')
                google = f'https://www.google.com/search?q={query}'
                webbrowser.open(google)
            else: continue





    print('\nAll mods have been iterated!')
    input('Done. Press ENTER to close...')
