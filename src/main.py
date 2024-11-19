import tkinter as tk
from tkinter import filedialog
from src.scanner.scanner import Scanner

def browse_and_read_file():
    # Create a Tkinter root window (hidden)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog to select the file
    file_path = filedialog.askopenfilename(title="Select a File",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    if file_path:  # If a file was selected
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()  # Read the file content
                return content
        except Exception as e:
            print(f"Error reading file: {e}")
            return None
    else:
        print("No file selected.")
        return None


# Run the file browsing and reading function
code = browse_and_read_file()

if code:  # If content is successfully read
    # Create a Scanner object and tokenize the code
    try:
        scanner = Scanner(code)
        tokens = scanner.tokenize()

        # Print the tokens
        for token in tokens:
            print(token)
    except Exception as e:
        print(f"Error during tokenization: {e}")
else:
    print("No code provided.")
