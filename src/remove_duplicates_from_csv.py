import pandas as pd


def remove_duplicates(input_file, output_file):
    """
    Removes duplicates from the specified CSV file and saves the cleaned data to output_file.

    Parameters:
    input_file (str): The path to the input CSV file.
    output_file (str): The path to the output CSV file.
    """
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)

        # Remove duplicated rows
        df_cleaned = df.drop_duplicates()

        # Save the cleaned DataFrame to a new CSV file
        df_cleaned.to_csv(output_file, index=False)
        print(f"Duplicates removed. Cleaned file saved as '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{input_file}' is empty.")
    except pd.errors.ParserError:
        print(f"Error: The file '{input_file}' is not a valid CSV.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Usage example
if __name__ == "__main__":
    input_file = r'../out/merged_output.csv'
    output_file = r'../out/cleaned_output.csv'
    remove_duplicates(input_file, output_file)
