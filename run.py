import os
import logging
from add_logo.logo_adder import validate_image_format, produce_new_logo, process_logo


try:
    os.mkdir('Generated-Images')
except FileExistsError as e:
    logging.info("Directory 'Generated-Images' already exist. Going to next step.")


RAW_FILES = os.path.abspath('Raw-Images')
EDITED_FILES = os.path.abspath('Generated-Images')


def main():
    """Logo file have to be in same path as run.py"""

    # logo_path = produce_new_logo(
    #     logo_name='LOGO-BASE', # no need to provide extension for a file!
    #     desired_width=75,
    #     desired_height=75,
    #     new_logo_name='NOWE' # same here!
    #     )
    validate_image_format(
        image_name='NOWE.png',  
    )
    # process_logo(
    #     logo_name=logo_path,
    #     path_to_raw_files=RAW_FILES,
    #     path_to_edited_files=EDITED_FILES,
    #     placement='bottom-left'
    #     )
 

if __name__ == '__main__':
    main()


