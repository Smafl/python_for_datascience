import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    """
    Load an image, print its information,
    crop a square part from it and transpose it (rotate it 90 degrees
    clockwise using index mapping) and display a new image.
    """
    try:
        img = ft_load("array/ex04/animal.jpeg")
        if img.size == 0:
            return

        print(f"The shape of image is: {img.shape}")
        # np.set_printoptions(threshold=np.inf)
        print(img)

        zoomed_img = img[50:450, 100:500]  # y1:y2, x1:x2

        height = len(zoomed_img)
        width = len(zoomed_img[0])
        new_image = [[[0, 0, 0] for i in range(height)] for _ in range(width)]

        for i in range(height):
            for j in range(width):
                new_image[width - 1 - j][i] = zoomed_img[i][j]

        new_image = np.array(new_image, dtype=np.uint8)

        grayscaled_img = np.mean(new_image, axis=2, keepdims=True)

        print(f"New shape after slicing: {grayscaled_img.shape}")
        # np.set_printoptions(threshold=np.inf)
        print(new_image)

        plt.imshow(grayscaled_img.squeeze(), cmap="gray")
        plt.show()

    except Exception as error:
        print("An error occurred:", error)


if __name__ == "__main__":
    main()
