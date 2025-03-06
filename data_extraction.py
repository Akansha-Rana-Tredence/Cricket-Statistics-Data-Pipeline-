import kagglehub
import os
import pandas as pd

class KaggleDatasetManager:
    def __init__(self, dataset_name):
        self.dataset_name = dataset_name
        self.dataset_path = None
        self.df = None

    def download_dataset(self):
        """Download the Kaggle dataset."""
        self.dataset_path = kagglehub.dataset_download(self.dataset_name)
        print(f"Dataset downloaded at: {self.dataset_path}")

    def list_dataset_files(self):
        """List all files in the downloaded dataset directory."""
        if self.dataset_path:
            dataset_files = os.listdir(self.dataset_path)
            print("Files in dataset:", dataset_files)
            return dataset_files
        else:
            print("Dataset not downloaded yet.")
            return []

    def load_csv_to_dataframe(self):
        """Find the first CSV file and load it into a Pandas DataFrame."""
        dataset_files = self.list_dataset_files()
        csv_file = None

        for file in dataset_files:
            if file.endswith(".csv"):
                csv_file = os.path.join(self.dataset_path, file)
                break

        if csv_file:
            self.df = pd.read_csv(csv_file)
            print(self.df.head())
        else:
            print("\nNo CSV file found in the dataset.")

    def save_dataframe_to_project(self, output_filename="t20matches_data.csv"):
        """Save the DataFrame to the base project directory."""
        if self.df is not None:
            base_project_location = os.getcwd()  # Get current working directory
            output_file = os.path.join(base_project_location, output_filename)
            self.df.to_csv(output_file, index=False)
            print(f"DataFrame saved to: {output_file}")
        else:
            print("No DataFrame available to save.")

# Usage
if __name__ == "__main__":
    dataset_manager = KaggleDatasetManager("imrankhan17/t20matches")
    dataset_manager.download_dataset()
    dataset_manager.load_csv_to_dataframe()
    dataset_manager.save_dataframe_to_project()
