import cv2

class ImageProcessor:
    def __init__(self, filter_type, filter_size):
        self.filter_type = filter_type
        self.filter_size = filter_size

    def process_image(self, image):
        if self.filter_type == 'blur':
            return cv2.blur(image, (self.filter_size, self.filter_size))
        elif self.filter_type == 'edge_detection':
            return cv2.Canny(image, 100, 200)
        else:
            raise ValueError('Invalid filter type')