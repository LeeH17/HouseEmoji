import cv2
import sys
import os
import stitcher_class



"""
takes in the path to a folder containing 
images. Opens up each image and stores in 
a list. Using that list, makes a stitcher object
and attempts to construct a panorama using the 
make_panorama() function call on the Stitcher object
"""


folder = sys.argv[1]

img_list = os.listdir(folder)

os.chdir(folder)

images = []

for img in img_list:
	images.append(cv2.imread(img))

	
Pano = stitcher_class.Stitcher(images)
Pano.make_panorama()
	
	
	
	
	