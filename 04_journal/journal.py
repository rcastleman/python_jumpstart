"""intermedia interim journal.py"""

import os

def load(name):
    """
    
    This method creates and loads a new journal.
    :param name: base name of the journal to be loaded
    :return: a new journal populated with the file data
    
    """
    data = []
    filename = get_full_pathname(name)
    if os.path.exists(filename):
        with open(filename) as file_input:
            for entry in file_input.readlines():
                # print ("would load: " + entry.rstrip())
                data.append(entry.rstrip())
    return data

def save(name,journal_data):
    filename = get_full_pathname(name)
    print("....saving to: {}".format(filename))
    with open(filename,'w') as file_out: # automatically closes the file when the block completes
        for entry in journal_data:
            file_out.write(entry + '\n')

def add_entry(text,journal_data):
    journal_data.append(text)

def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.','journals/', name + '.jrl'))
    return filename
