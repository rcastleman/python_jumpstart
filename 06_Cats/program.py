import os

def main():
    print_header()

    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)

    # download cats
    # display cats

def print_header():
    print('')
    print('---------------------------------------')
    print('          CAT FACTORY                  ')
    print('---------------------------------------')

def get_or_create_output_folder():
    # print(__file__)
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder,folder)
    
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('creating new directory at {}'.format(full_path))
        os.makedirs(full_path)
    
    return full_path




if __name__ == '__main__':
    main()