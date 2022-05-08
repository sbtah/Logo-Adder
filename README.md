# Logo Adder - Made by Grzegorz Zygan

Simple project created in Python and pillow library, made for my former employer.
Main goal of this program is to add logotype to larch pool of images.

- Program validates logo file and scale it to desired size with produce_new_logo() method.
- It also loops over all images located in 'Raw-Images' folder, paste the specified logo on specified location and then stores new files in 'Generated-Images' folder.

Todo:
- Verify size and type of image file and resize and save to proper format if needed.