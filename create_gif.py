import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ['pics/roar1.png', 'pics/roar2.png', 'pics/roar3.png', 'pics/roar4.png', 'pics/roar5.png', 'pics/roar6.png']
images = []

# Function to resize images to a common size
def process_image(image_path, target_size=(500, 300)):
    with Image.open(image_path) as img:
        # Convert image to RGB mode if it's not already
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Resize the image
        img = img.resize(target_size, Image.LANCZOS)

        img_array = np.array(img)

        return img_array

# Resize all images to target size
for filename in filenames:
    images.append(process_image(filename))

# Create the gif
iio.imwrite('roar.gif', images, duration = 500, loop = 0)