import os

# DEBUG for now:
# __file__ = os.getcwd()+'\\mod-organizer-redownloader'


DIRECTORY = os.path.dirname(__file__) + '\\categories' # Directory is GIVEN BY USER

def get_categories():
    categories = {}

    # Make the category directory if it doesn't exist
    os.makedirs(DIRECTORY, exist_ok=True)
    for file in os.listdir(DIRECTORY):
        if file.endswith('.cat'):
            with open(DIRECTORY+ '\\' + file, 'r') as owo:
                if owo.readline() == FIRST_LINE:
                    for line in owo:
                        # line[:-1] to remove newline char
                        line = line[:-1]
                        if not line.startswith('//'):
                            try:
                                # Get category and items
                                category, items = line.split(' = ')
                                # Create items list, and make sure to strip any extraneous spaces
                                if isinstance(items, str):
                                    items = [items.strip()]
                                else:
                                    items = [item.strip() for item in items]
                                if category in categories:
                                    print('WARNING: Overwriting category already set.')
                                categories[category] = items
                                # print(category, items)
                            except ValueError:
                                # Invalid line, ignore for now
                                print('WARNING: Invalid line in file {}, if you haven\'t edited the file, report this error to the developer (Along with the file!)'.format(file))
                            except Exception as e:
                                print('Error: {}'.format(e))
                            # print(line)
                else: print('Invalid File in directory: {} [IGNORING]'.format(file))

    # This one-liner inverts the dictionary, offering the ability to search for category based on file extension
    # This line is very case-specific so don't copy-paste to other projects!!
    categories = {value: key for key in categories for value in categories[key]}
    return categories


def test_functions():
    print('Testing get_categories:')
    categories = get_categories()
    print(str(categories)+'\n')


#test_functions()
