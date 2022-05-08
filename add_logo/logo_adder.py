import os
import PIL
import logging
from PIL import Image



logging.basicConfig(level=logging.INFO)


def produce_new_logo(logo_file, width, height, new_logo_name):
    """Resize old logo to desired size and provide path to new one"""

    desired_size = width, height

    try:
        logo = Image.open(f'{logo_file}.png')
        if logo.size != desired_size:
            logo.thumbnail(desired_size, resample=Image.Resampling.LANCZOS)
            logo.save(f'{new_logo_name}.png')
            logo.close()
        else:
            logging.info("Current logo file doesn't have to be resized.")
    except FileNotFoundError as e:
        logging.info('Sorry file you specified cannot be found')
    
    return os.path.abspath(f'{new_logo_name}.png')


def process_logo(logo_name, path_to_raw_files, path_to_edited_files,  placement):
    """
    Paste logo file on specified image.
    placement can have 4 values:
    'top-left', 'top-right'
    'bottom-left, 'bottom-right'
    """

    os.chdir(path_to_raw_files)

    if os.listdir() == ['README.txt']:
        logging.info("No images to process")
    else:
        for file in os.listdir():
            if file == 'README.txt':
                continue
            else:
                try:
                    image = Image.open(os.path.abspath(file))
                    logo = Image.open(f'{logo_name}')
                    image_width, image_height = image.size
                    logo_width, logo_height = logo.size

                    if placement == 'top-left':
                        image.paste(logo, (0, 0), logo)
                        os.chdir(path_to_edited_files)
                        image.save(f'EDITED-{file}')
                        os.chdir(path_to_raw_files)
            
                    elif placement == 'bottom-right':
                        image.paste(logo, (image_width - logo_width, image_height - logo_height), logo)
                        os.chdir(path_to_edited_files)
                        image.save(f'EDITED-{file}')
                        os.chdir(path_to_raw_files)

                    elif placement == 'top-right':
                        image.paste(logo, (image_width - logo_width, 0), logo)
                        os.chdir(path_to_edited_files)
                        image.save(f'EDITED-{file}')
                        os.chdir(path_to_raw_files)

                    elif placement == 'bottom-left':
                        image.paste(logo, (0, image_height - logo_height), logo)
                        os.chdir(path_to_edited_files)
                        image.save(f'EDITED-{file}')
                        os.chdir(path_to_raw_files)
                except PIL.UnidentifiedImageError as e:
                    logging.error("Files in Raw-Images have to be a JPG or PNG format.")

