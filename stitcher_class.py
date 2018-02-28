import cv2

class Stitcher(object):

	
	
	def __init__(self, images):
		""" 
		creates a stitcher object that saves a list of images
		and creates an OpenCV stitcher object
		"""
		
		self.images = images
		self.stitcher = cv2.createStitcher(False)
		
	def make_panorama(self):
		"""
		Puts the images in the stitches image list 
		together into a panorama
		"""
		
		
		# if there is more than one image attempt 
		# to stitch them together 
		if len(self.images) > 1:
			
			#stitch images together
			self.pano = self.stitcher.stitch(self.images)
		
		
			'''
			 pano is a tuple
			 pano[0] is an error code, 
			
			 if pano[0] == 0 --> OK
			 if pano[0] == 1 --> ERR_NEED_MORE_IMGS
			 if pano[0] == 2 --> ERR_HOMOGROPHY_EST_FAIL
			 if pano[0] == 3 --> ERR_CAMERA_PARAMS_ADJUST_FAIL
			
			 pano[1], if operation successful is the panorama image
			'''
			
			
			# Write panorama to current wd to see results
			#if self.pano[0] == 0:
				#cv2.imwrite("pano.jpg", self.pano[1])
			

			