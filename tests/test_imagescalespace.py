#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import sys

import imagescalespace.imagescalespace as imagescalespace

from PIL import Image
import numpy as np
from scipy import misc

SmallValue = 1E-24

def save_as_image( filename, array ):
	t = np.copy( array )
	t = np.clip( t, 0.0, 1.0 ) * 255.
	t = t.astype( np.uint8 )
	Image.fromarray( t ).save( '__tests__'+filename )

class tests( unittest.TestCase ):
###################################################################
	@classmethod
	def setUpClass(cls): # it is called before test starting
		pass

	@classmethod
	def tearDownClass(cls): # it is called before test ending
		#for file in glob.glob('__tests__*'):
		#	os.remove(file)
		pass

	def setUp(self): # it is called before each test
		self.array = misc.face().astype( np.float32 ) / 255.0
		save_as_image( 'face.png', self.array )
		pass

	def tearDown(self): # it is called after each test
		pass
                
###################################################################
	def test_dim3(self):
		level = 3
		ss = imagescalespace.decomp( self.array, level = level, dims_outputs = 3 )
		self.assertEqual( ss.shape[2], level*self.array.shape[2] )
		
		ar = imagescalespace.comp( ss, nb_channels=self.array.shape[2] )
		dif = ar - self.array
		dif = np.square( np.mean( np.square( dif ) ) )
		self.assertLess( dif, SmallValue )

		ar = imagescalespace.comp( ss, level=level )
		dif = ar - self.array
		dif = np.square( np.mean( np.square( dif ) ) )
		self.assertLess( dif, SmallValue )

	def test_dim4(self):
		level = 4
		ss = imagescalespace.decomp( self.array, level = level, dims_outputs = 4 )
		self.assertEqual( ss.shape[3], level )
		ar = imagescalespace.comp( ss )
		
		for i in range(1,level):
			save_as_image( 'face_level{i:d}.png'.format(i=i), ss[:,:,:,i]+0.5 )
		save_as_image( 'face_level0.png', ss[:,:,:,0] )
		save_as_image( 'face_comp.png', ar )
		
		dif = ar - self.array
		dif = np.square( np.mean( np.square( dif ) ) )
		
		self.assertLess( dif, SmallValue )


###################################################################
	def suite():
		suite = unittest.TestSuite()
		suite.addTests(unittest.makeSuite(tests))
		return suite
  
if( __name__ == '__main__' ):
	unittest.main()
