import cv2
import numpy as np
from multiprocessing import Pool
from image_processor import ImageProcessor
from image_io import load_image, save_image

def process_image(image_path, filter_type, filter_size):
    image = load_image(image_path)
    processor = ImageProcessor(filter_type, filter_size)
    processed_image = processor.process_image(image)
    save_image(processed_image, 'processed_' + image_path)

def main():
    image_path = 'image.jpg'
    filter_type = 'blur'
    filter_size = 5

    image = load_image(image_path)

    chunk_size = 100
    chunks = [image[i:i+chunk_size, j:j+chunk_size] for i in range(0, image.shape[0], chunk_size) for j in range(0, image.shape[1], chunk_size)]

    with Pool(processes=4) as pool:
        processed_chunks = pool.map(ImageProcessor(filter_type, filter_size).process_image, chunks)

    processed_image = np.zeros_like(image)
    for i in range(len(chunks)):
        processed_image[i*chunk_size:(i+1)*chunk_size, i*chunk_size:(i+1)*chunk_size] = processed_chunks[i]

    save_image(processed_image, 'processed_' + image_path)

if __name__ == '__main__':
    main()