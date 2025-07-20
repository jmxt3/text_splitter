# Large File Splitter

A simple, command-line Python utility to split large text or binary files into smaller, more manageable chunks. This is useful for breaking down large log files, datasets, or any file that exceeds size limits for uploading, processing, or emailing.

## Features

- Splits any file into smaller parts based on a specified chunk size.
- Works with both text and binary files.
- Simple and intuitive command-line interface.
- No external dependencies required (uses only Python's standard library).

## Requirements

- Python 3.6+

## Installation

1.  **Get the script:**
    Clone the repository or simply download the `main.py` script to a directory on your computer.

2.  **Set up your environment (Optional but Recommended):**
    This script has no external dependencies. However, using a tool like `uv` to run it in a managed environment is a good practice.

    If you don't have `uv`, you can install it:
    ```bash
    # On macOS and Linux
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # On Windows (in PowerShell)
    irm https://astral.sh/uv/install.ps1 | iex
    ```

## Usage

Run the script from your terminal, providing the path to the file you want to split. The output chunks will be created in the same directory as the source file.

### Command-Line Arguments

-   `file_path`: (Required) The path to the large file you want to split.
-   `-s, --size`: (Optional) The maximum size of each chunk in bytes. Defaults to `524288` (0.5 MB).

### Examples

1.  **Basic Splitting**

    To split a file named `large_log_file.log` using the default chunk size of 0.5 MB:

    ```bash
    # Using uv (recommended)
    uv run python main.py path/to/large_log_file.log

    # Or using your system's Python
    python main.py path/to/large_log_file.log
    ```

2.  **Splitting with a Custom Chunk Size**

    To split `my_dataset.csv` into 1MB chunks (`1048576` bytes):

    ```bash
    # Using uv
    uv run python main.py path/to/my_dataset.csv --size 1048576

    # Using your system's Python
    python main.py path/to/my_dataset.csv -s 1048576
    ```

3.  **Windows Example**

    If your file `git_scape_django_digest.txt` is in the current directory, you can run:

    ```powershell
    # This command splits the file into default-sized (0.5 MB) chunks
    uv run python main.py git_scape_django_digest.txt
    ```

### Output

Splitting a file named `my_file.txt` will produce `my_file_part_1.txt`, `my_file_part_2.txt`, and so on, in the same directory.