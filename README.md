# CSV Manipulations in Python

This project demonstrates how to manipulate CSV files using Python. It includes scripts to merge multiple CSV files and to remove duplicates from a CSV file.

## Project Structure

```txt
csv-manipulations-python/
│
├── csv/ # Folder containing CSV files
│ ├── data1.csv
│ ├── data2.csv
│ └── data3.csv
│
├── out/ # Folder for output files
│ ├── cleaned_output.csv
│ └── merged_output.csv
│
├── src/ # Source code folder
│ ├── merge_csv_files.py
│ └── remove_duplicates_from_csv.py
│
├── README.md # Project documentation
└── requirements.txt # Dependencies
```


## Setup

### Prerequisites

Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

### Merging CSV Files

The `merge_csv_files.py` script merges all CSV files in the `csv` folder into a single file.

**Command:**

```bash
python src/merge_csv_files.py
```

**Output:**

The merged output will be saved to `out/merged_output.csv`.

### Removing Duplicates

The `remove_duplicates_from_csv.py` script removes duplicates from the specified CSV file.

**Command:**

```bash
python src/remove_duplicates_from_csv.py
```

**Output:**

The cleaned file with duplicates removed will be saved to `out/cleaned_output.csv`.

## Script Details

### `merge_csv_files.py`

This script reads all CSV files from the specified folder, merges them into a single DataFrame, and saves the merged DataFrame to an output CSV file.

**Function: `merge_csv_files`**

```python
def merge_csv_files(folder_path, output_file):
    """
    Merges all CSV files in the specified folder into a single DataFrame and saves to output_file.

    Parameters:
    folder_path (str): The path to the folder containing the CSV files.
    output_file (str): The path to the output CSV file.
    """
```

### `remove_duplicates_from_csv.py`

This script removes duplicate rows from the specified CSV file and saves the cleaned DataFrame to an output CSV file.

**Function: `remove_duplicates`**

```python
def remove_duplicates(input_file, output_file):
    """
    Removes duplicates from the specified CSV file and saves the cleaned data to output_file.

    Parameters:
    input_file (str): The path to the input CSV file.
    output_file (str): The path to the output CSV file.
    """
```

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Copyright



© 2022 **[Lahcen Ezzara](https://lahcenezzara.github.io)**. All rights reserved.

This project is licensed under the MIT License.
