# divide_image.py ${image_file_name} ${column_num} ${row_num} ${prefix_output_filename}
# divide_image.py divide_image_py 3 4 test

# homebrew 사용중, pip3
# pip3 install pillow

# M1 chip scipy
# https://stackoverflow.com/questions/65745683/how-to-install-scipy-on-apple-silicon-arm-m1

# pip3 install --upgrade pip setuptools wheel
# pip3 install -U albumentations 


from PIL import Image, ImageOps
import numpy as np
import random
import torchvision.transforms as transforms
import albumentations as A
import cv2
import sys
import glob


def divide_image(height, rowpix, width, colpix, prefix_output_filename, np_im, suffix_list):
    i = 0
    for r in range(0, height, rowpix):

        for c in range(0, width, colpix):
            output_filename = f'{prefix_output_filename}{suffix_list[i]}.jpeg'

            image = np_im[r:r+rowpix, c:c+colpix, :]
            '''
            transform = A.Compose([
                A.HorizontalFlip(p=0.5),
                A.VerticalFlip(p=0.5),
                A.RandomRotate90(p=0.5)
            ])

            # <class 'numpy.ndarray'>
            transformed_image = transform(image=image)["image"]

            transformed_image = Image.fromarray(transformed_image).convert('RGB')
            transformed_image.save(output_filename)
            '''
            Image.fromarray(image).save(output_filename)

            i += 1

def process_input(image_file_name, column_num, row_num, prefix_output_filename):
    im = Image.open(image_file_name)
    np_im = np.asarray(im)

    height, width, depth = np_im.shape

    num_of_tiles = row_num*column_num
    rowpix, colpix = height//row_num, width//column_num

    # https://towardsdatascience.com/efficiently-splitting-an-image-into-tiles-in-python-using-numpy-d1bf0dd7b6f7

    tiles = [[] for i in range(num_of_tiles)]
    suffix_list = random.sample(range(num_of_tiles), num_of_tiles)
    #suffix_list = [i for i in range(num_of_tiles)]
    #print(suffix_list)

    divide_image(height, rowpix, width, colpix, prefix_output_filename, np_im, suffix_list)
    
    
def main():
    image_file_name, column_num, row_num, prefix_output_filename = list((sys.argv))[1:]
    
    column_num, row_num = int(column_num), int(row_num)

    image_file_name = glob.glob(f'{image_file_name}.*')[0]
    
    process_input(image_file_name, column_num, row_num, prefix_output_filename)


if __name__ == '__main__':
    main()
                            

