import pandas as pd
import os


def load(path: str) -> pd.DataFrame | None:
    """
    Write the dimensions of the dataset and return the dataset.

    Args:
        path (str): A path to the dataset.

    Returns:
        pd.DataFrame or None: Loaded dataset, or None if error occurs.
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")

        dataset = pd.read_csv(path)

        print(f"Loading dataset of dimensions {dataset.shape}")

        return dataset

    except Exception as error:
        print("An error occurred:", error)
        return None
