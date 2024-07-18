import pandas as pd
import os


def merge_csv_files(folder_path, output_file):
    """
    Merges all CSV files in the specified folder into a single DataFrame and saves to output_file.

    Parameters:
    folder_path (str): The path to the folder containing the CSV files.
    output_file (str): The path to the output CSV file.
    """
    try:
        # List to hold DataFrames
        dfs = []

        # Check if the folder exists
        if not os.path.exists(folder_path):
            print(f"Error: The folder '{folder_path}' does not exist.")
            return

        # Iterate over all CSV files in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith(".csv"):
                file_path = os.path.join(folder_path, filename)
                try:
                    # Read the CSV file into a DataFrame
                    df = pd.read_csv(file_path)
                    # Append the DataFrame to the list
                    dfs.append(df)
                    print(f"Successfully read '{filename}'.")
                except pd.errors.EmptyDataError:
                    print(f"Warning: '{
                          filename}' is empty and will be skipped.")
                except pd.errors.ParserError:
                    print(f"Warning: '{
                          filename}' is not a valid CSV and will be skipped.")

        if not dfs:
            print("Error: No valid CSV files found in the folder.")
            return

        # Concatenate all DataFrames in the list into a single DataFrame
        merged_df = pd.concat(dfs, ignore_index=True)

        # Save the merged DataFrame to a new CSV file
        merged_df.to_csv(output_file, index=False)
        print(f"Merged DataFrame saved to '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Usage example
if __name__ == "__main__":
    folder_path = r'../csv'
    output_file = r'../out/merged_output.csv'
    merge_csv_files(folder_path, output_file)
