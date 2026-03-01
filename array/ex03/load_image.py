import os
from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Load an image,
    convert it to RGB format and
    print the shape of the image in the form (height, width, channels).

    Args:
        path (str): Path to an image.

    Returns:
        np.ndarray: A NumPy array containing the image pixels in RGB format.
                    Returns an empty array if an error occurs.
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")

        with Image.open(path) as img:
            img = img.convert("RGB")
            img_array = np.array(img)

        return img_array

    except Exception as error:
        print("An error occurred:", error)
        return np.array([])
