import pandas as pd
import os
from config import DATA_PATH

class DataLoader:
    """
    Handles loading and preprocessing of UPS facility data.
    """

    def __init__(self, file_path=DATA_PATH):
        """
        Initializes the DataLoader.

        Parameters:
        - file_path (str): Path to the UPS facility dataset.
        """
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """
        Loads UPS facility data from a CSV file.

        Returns:
        - pd.DataFrame: A DataFrame containing the loaded dataset.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Dataset not found at {self.file_path}")

        self.data = pd.read_csv(self.file_path)
        return self.data

    def get_facilities(self):
        """
        Extracts relevant columns from the dataset.

        Returns:
        - pd.DataFrame: A DataFrame containing only essential facility details.
        """
        if self.data is None:
            self.load_data()

        return self.data[["NAME", "LATITUDE", "LONGITUDE"]]

# Usage Example
if __name__ == "__main__":
    data_loader = DataLoader()
    facilities = data_loader.get_facilities()
    print(f"Loaded {len(facilities)} UPS facilities.")
