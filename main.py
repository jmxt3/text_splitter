import os
import argparse

__author__ = "Joao Machete"

def split_file(file_path, chunk_size=524288):
    """
    Splits a large file into smaller chunks of a specified size.

    Args:
        file_path (str): The path to the large file to be split.
        chunk_size (int): The maximum size of each chunk in bytes.
                          Default is 524,288 bytes (0.5 MB).
    """
    # --- 1. Input Validation ---
    if not os.path.exists(file_path):
        print(f"Error: File not found at '{file_path}'")
        return

    if os.path.getsize(file_path) == 0:
        print(f"Warning: The file '{file_path}' is empty. No chunks will be created.")
        return

    # --- 2. Setup for Splitting ---
    # Get the directory and the base name of the input file
    file_dir, file_name = os.path.split(file_path)
    base_name, extension = os.path.splitext(file_name)

    # Counter for the output files
    part_num = 1

    # --- 3. Read and Write Chunks ---
    try:
        # Open the large file for reading in binary mode ('rb')
        with open(file_path, 'rb') as f_in:
            while True:
                # Read a chunk of the specified size
                chunk = f_in.read(chunk_size)

                # If the chunk is empty, we've reached the end of the file
                if not chunk:
                    break

                # --- 4. Create and Write to Output File ---
                # Define the output filename
                output_filename = f"{base_name}_part_{part_num}{extension}"
                output_path = os.path.join(file_dir, output_filename)

                print(f"Creating chunk: {output_path}")

                # Open the chunk file for writing in binary mode ('wb')
                with open(output_path, 'wb') as f_out:
                    f_out.write(chunk)

                # Increment the part number for the next chunk
                part_num += 1

        print("\nFile splitting completed successfully!")

    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to parse command-line arguments and run the splitter.
    """
    # --- 5. Command-Line Interface Setup ---
    parser = argparse.ArgumentParser(
        description="A command-line utility to split a large file into smaller, more manageable chunks.",
        formatter_class=argparse.RawTextHelpFormatter, # For better help text formatting
        epilog=f"Author: {__author__}"
    )

    parser.add_argument(
        "file_path",
        type=str,
        help="The path to the large file you want to split."
    )

    parser.add_argument(
        "-s", "--size",
        type=int,
        default=524288,
        help="The maximum chunk size in bytes.\nDefault is 524288 (0.5 MB)."
    )

    args = parser.parse_args()

    # Call the main splitting function with the provided arguments
    split_file(args.file_path, args.size)

# --- 6. Script Execution ---
if __name__ == "__main__":
    # Example of how to run from the command line:
    # python your_script_name.py /path/to/your/largefile.txt
    #
    # To specify a different chunk size (e.g., 1MB):
    # python your_script_name.py /path/to/your/largefile.txt --size 1048576
    main()
