# all possible RGB colors pixel as png files in ./RGB-colors/png/
import os
import numpy as np
from PIL import Image

# create directory if not exists
if not os.path.exists('RGB-colors/png'):
    os.makedirs('RGB-colors/png')

    # check if the RGB numbers file exists
if os.path.exists('RGB-colors/rgb_numbers.txt'):
    # read the RGB numbers from the file
    with open('RGB-colors/rgb_numbers.txt', 'r') as file:
        rgb_numbers = file.readlines()
    # get the last stored RGB value
    last_rgb = rgb_numbers[-1].strip().split()
    last_r, last_g, last_b = map(int, last_rgb)
    # continue creating pixels from the last stored value
    for r in range(last_r, 256):
        for g in range(last_g, 256):
            for b in range(last_b, 256):
                # save the RGB numbers to the text file
                with open('RGB-colors/rgb_numbers.txt', 'a') as file:
                    file.write(f'{r} {g} {b}\n')
                img = Image.new('RGB', (1, 1), (r, g, b))
                img.save('RGB-colors/png/%d_%d_%d.png' % (r, g, b))
else:
    # create all possible RGB colors pixel as png files
    for r in range(256):
        for g in range(256):
            for b in range(256):
                # save the RGB numbers to a text file
                with open('RGB-colors/rgb_numbers.txt', 'w') as file:
                    file.write(f'{r} {g} {b}\n')
                img = Image.new('RGB', (1, 1), (r, g, b))
                img.save('RGB-colors/png/%d_%d_%d.png' % (r, g, b))
    
os.system('rm RGB-colors/rgb_numbers.txt')
