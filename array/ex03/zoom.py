import numpy as np
import matplotlib.pyplot as plt
import ft_load


def main():
    """
    Load an image, display its information, apply a zoom using NumPy slicing,
    convert the zoomed region to grayscale, and display the result.
    """
    try:
        img = ft_load("array/ex03/animal.jpeg")
        if img.size == 0:
            return

        print(f"The shape of image is: {img.shape}")
        # np.set_printoptions(threshold=np.inf)
        print(img)

        zoomed_img = img[50:400, 100:500]  # y1:y2, x1:x2
        grayscaled_img = np.mean(zoomed_img, axis=2, keepdims=True)

        print(f"New shape after slicing: {grayscaled_img.shape}")
        # np.set_printoptions(threshold=np.inf)
        print(zoomed_img)

        plt.imshow(grayscaled_img.squeeze(), cmap="gray")
        plt.show()

    except Exception as error:
        print("An error occurred:", error)


if __name__ == "__main__":
    main()
