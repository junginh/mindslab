# merge_image.py ${input_filename_prefix} ${column_num} ${row_num} ${output_filename}
# merge_image.p test 2 2 merged


import os
import glob
from PIL import Image
import sys
import numpy as np


def merge_image(column_num, row_num, height, width, imagelist, output_filename):
    new_im = Image.new('RGB', (width*column_num, height*row_num))
    
    y_offset = 0
    count = 0

    '''
    for i in imagelist:
        im=Image.open(i)
        print('here')
        display(im)
    '''

    for r in range(row_num):

        x_offset = 0

        for c in range(column_num):
            #print(count, x_offset, y_offset)
            im=Image.open(imagelist[count])
            new_im.paste(im, (x_offset, y_offset))
            x_offset += im.size[0]
            count += 1
        y_offset += im.size[1]
    new_im.save(output_filename)


def get_merge_dimension(image, column_num, row_num):
    im = Image.open(image)
    np_im = np.asarray(im)
    height, width, depth = np_im.shape
    

    return (height, width)
    


def main():
    input_filename_prefix, column_num, row_num, prefix_output_filename = list((sys.argv))[1:]
    column_num, row_num = int(column_num), int(row_num)
    output_filename = prefix_output_filename +'.jpeg'

    # + does not work [0-9][0-9]* does not work
    #print(glob.glob(f'{input_filename_prefix}[0-9]+.jpeg'))
    imagelist = glob.glob(f'/Users/junginhong/mindslab/{input_filename_prefix}[0-9]*.jpeg')
    
    
    height, width = get_merge_dimension(imagelist[0], column_num, row_num)
    
    merge_image(column_num, row_num, height, width, imagelist, output_filename)

if __name__ == '__main__':
    main()
