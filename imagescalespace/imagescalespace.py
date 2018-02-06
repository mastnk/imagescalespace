#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scipy import ndimage
import numpy as np

def gaussian_blur( input, blur_sigma ):
	return ndimage.gaussian_filter(input, sigma=[blur_sigma,blur_sigma,0], truncate=3.0, mode='nearest' )

def decomp( input, level, blur_sigma=2.5, dims_outputs=4 ):
	if( not isinstance( input, np.ndarray) ):
		msg = 'The input should be numpy.ndarray.'
		raise TypeError( msg )

	if( dims_outputs < 3.5 ):
		dims_outputs = 3
	else:
		dims_outputs = 4
	
	I = np.copy( input )
	output = np.zeros( input.shape + (level,), dtype=input.dtype )
	for level in range( level-1, 0, -1 ):
		L = gaussian_blur( I, blur_sigma )
		H = I-L
		I = L
		output[:,:,:,level] = np.copy(H)
	output[:,:,:,0] = np.copy(I)
	
	if( dims_outputs == 3 ):
		output_shape = output.shape
		output = np.reshape( output, ( output_shape[0], output_shape[1], output_shape[2]*output_shape[3] ) )
	
	return output

def comp( input, nb_channels = None, level = None ):
	if( not isinstance( input, np.ndarray) ):
		msg = 'The input should be numpy.ndarray.'
		raise TypeError( msg )

	input_shape = input.shape
	if( len( input_shape ) == 3 ):
		if( nb_channels is None ):
			if( level is None ):
				msg = 'nb_channels or level should be specified.'
				raise ValueError(msg)
			else:
				if( input_shape[2] % level != 0 ):
					msg = 'level is not matched.'
					raise ValueError(msg)
				output = np.reshape( input, (input_shape[0], input_shape[1], input_shape[2]//level, level ) )
		else:
			if( level is None ):
				if( input_shape[2] % nb_channels != 0 ):
					msg = 'nb_channels is not matched.'
					raise ValueError(msg)
				output = np.reshape( input, (input_shape[0], input_shape[1], nb_channels, input_shape[2]//nb_channels ) )
			else:
				if( input_shape[2] != nb_channels * level ):
					msg = 'nb_channels and level are not matched.'
					raise ValueError(msg)
				output = np.reshape( input, (input_shape[0], input_shape[1], nb_channels, nb_channels, level ) )
		
		output = np.sum( output, axis=3 )
		
	elif( len( input_shape ) == 4 ):
		output = np.sum( input, axis=3 )
	
	else:
		msg = 'The dims of input should be three or four.'
		raise ValueError( msg )
	
	return output
