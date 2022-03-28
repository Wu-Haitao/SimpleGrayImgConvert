from PIL import Image
import os
import sys


def convert_to_gray_img(path):
    img_in = Image.open(path)
    img_out = img_in.convert('L')
    f_name, f_ex_name = os.path.splitext(path)
    new_f_name = f_name + "_gray.png"
    img_out.save(new_f_name)
    print("Output file: ", new_f_name)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Parameters not match")
    else:
        print("Input file: ", sys.argv[1])
        convert_to_gray_img(sys.argv[1])
