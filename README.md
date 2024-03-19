# Parallelized Image Filter Application
<p align="center"> <img src="example.gif" alt="Example of Parallelized Image Filter Application"> </p>
This project demonstrates the efficient use of multithreading to accelerate image processing tasks using Python and the OpenCV library. It applies a filter to an image using a parallelized approach based on the map-reduce paradigm.

## Requirements
To run this project, you need to install the following libraries:
*OpenCV: 'pip install opencv-python'
*NumPy: 'pip install numpy'

## Usage
To use the project, simply execute the 'main.py' file:
~~~~
python main.py
~~~~
The program will load an image, apply a filter to it, and save the processed image to disk. The processed image will be saved as 'processed_<image_name>'.

Detailed instructions and code examples can be found in the project's documentation [here](docs/README.md).

## Implementation
The project consists of three main code files:
1. * 'main.py': This file orchestrates the image processing task, loads and saves images, and measures performance. It divides the image into smaller chunks, processes each chunk in parallel using a multiprocessing Pool, and combines the processed chunks to form the final processed image.
2. * 'image_processor.py': This file contains the image processing functions. It defines a class called 'ImageProcessor' that takes a filter type and size as input and processes the image using the specified filter.
3. * 'image_io.py': This file handles image loading and saving functionality. It defines two functions, 'load_image' and 'save_image', to load and save images using the OpenCV library.

The 'main.py' file performs the following steps:
* Loads an image from disk using the 'load_image' function from 'image_io.py'.
* Divides the image into smaller chunks of size 100x100.
* Processes each chunk in parallel using a multiprocessing Pool.
* Combines the processed chunks to form the final processed image.
* Saves the processed image to disk using the 'save_image' function from 'image_io.py'.

  The 'image_processor.py' file defines the 'ImageProcessor' class, which takes a filter type and size as input and processes the image using the specified filter. The following filter types are supported:

  * 'blur': Applies a blur filter to the image.
  * 'edge_detection': Applies an edge detection filter to the image.

## Performance Metrics
The program measures the execution time of the parallelized image processing compared to a sequential implementation. It records and analyzes the speedup achieved through parallelization.

## Error Handling
The program implements error handling mechanisms for robustness. If an invalid filter type is specified, the program raises a 'ValueError' with a message indicating the invalid filter type.

## Additional Considerations
The program can be extended to support different filter types and sizes, as well as dynamic load balancing strategies to distribute work more efficiently among worker processes.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
This project uses the OpenCV library for image processing and the multiprocessing library for parallel processing.
