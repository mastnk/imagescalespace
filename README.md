imagescalespace
====

It is a python package of scalespace.
The scale space is built by L_k = G( L_{k+1} ), H_k = L_{k+1} - L_k, where G represents a gaussian blur.
If you specify level=Q, L_Q is to be an input data and L_0 is lowest frequency data.

## Usage

### Import sample
`import imagescalespace.imagescalespace as scalespace`

### imagescalespace.imagescalespace.decomp( input, level, blur_sigma=2.5, dims_outputs=4 )
Decompose the input to scale space data.

- **input** *numpy.ndarray*
Three dimensional array of [height, width, channel]. Note that it should be three dimensional array even if it is a gray image data.

- **blur_sigma** *float*
It specifies the standard deviation of Gaussian blur kernel.

- **dims_outputs** *int*
It specifies dimensions of output data.

- **output** *numpy.ndarray*
If dims_outputs is 4, 4th dimension represents level of scalespace. If dims_output is 3, the four-dimensional output data is reshaped with (height, width, channel*level).


### imagescalespace.imagescalespace.comp(input, nb_channels = None, level = None )
Compose the scalespace data to the image.

- **input** *numpy.ndarray*
It should be three dimensional or four dimensional data.

- **nb_channels** *float*
If the input data is the three dimensional data, nb_channels and/or level should be specified. For the four dimensional input data, it is ignored.

- **level** *numpy.ndarray*
If the input data is the three dimensional data, nb_channels and/or level should be specified. For the four dimensional input data, it is ignored.

## Install

`% pip install git+https://github.com/mastnk/imagescalespace`

## Author

[Masayuki Tanaka](https://github.com/mastnk)
