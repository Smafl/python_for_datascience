import numpy as np
from PIL import Image


def ft_invert(array) -> np.array:
    """
    Invert an RGB image.
    Each pixel channel is replaced by its complement (255 - original value).

    Args:
        array (np.array): Original RGB image as a Numpy array.

    Returns:
        np.array: Inverted RGB image with the same shape (H, W, 3),
                  each pixel channel replaced by
                  its complement (255 - original value).
    """
    invert_array = array.copy()
    invert_array = 255 - array
    Image.fromarray(invert_array).show()
    return invert_array


def ft_red(array) -> np.array:
    """
    Keep only the red channel of an RGB image.
    Green and blue channels are set to zero.

    Args:
        array (np.array): Original RGB image as a Numpy array.

    Returns:
        np.array: RGB image with only the red channel preserved.
    """
    red_array = array.copy()
    red_array[::, ::, 1:3] = 0
    Image.fromarray(red_array).show()
    return red_array


def ft_green(array) -> np.array:
    """
    Keep only the green channel of an RGB image.
    Red and blue channels are set to zero.

    Args:
        array (np.array): Original RGB image as a Numpy array.

    Returns:
        np.array: RGB image with only the green channel preserved.
    """
    green_array = array.copy()
    green_array[::, ::, 0:1] = 0
    green_array[::, ::, 2:3] = 0
    Image.fromarray(green_array).show()
    return green_array


def ft_blue(array) -> np.array:
    """
    Keep only the blue channel of an RGB image.
    Red and green channels are set to zero.

    Args:
        array (np.array): Original RGB image as a Numpy array.

    Returns:
        np.array: RGB image with only the blue channel preserved.
    """
    blue_array = array.copy()
    blue_array[::, ::, 0:2] = 0
    Image.fromarray(blue_array).show()
    return blue_array


def ft_grey(array) -> np.array:
    """
    Convert an RGB image to grayscale.
    Each pixel's R, G, B channels are replaced by the pixel's
    average brightness.

    Args:
        array (np.array): Original RGB image as a Numpy array.

    Returns:
        np.array: Grayscale image with the same shape (H, W, 3),
                  each pixel's channels equal to the original pixel mean.
    """
    gray_array = array.copy()
    gray_mean = np.mean(gray_array, axis=2, keepdims=True)
    gray_array[:, :, :] = gray_mean
    Image.fromarray(gray_array).show()
    return gray_array
