import Augmentor
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--loc', help='Put the location of the images', default=None)
arg_parser.add_argument('--num', help='Put the output number of images', default=None)
args = arg_parser.parse_args()
img_loc = args.loc
img_num = args.num


p = Augmentor.Pipeline((img_loc))

p.random_brightness(probability=1, min_factor=0.3, max_factor=1.5)
p.zoom(probability=1, min_factor=0.5, max_factor=2.3)
p.flip_left_right(probability=1)
p.shear(probability=1, max_shear_left=15, max_shear_right=15)
p.skew(probability=0.5, magnitude=0.2)
p.random_contrast(probability=1, min_factor=0.5, max_factor=1.8)
p.sample (int(img_num)) 