import tkinter as tk
from tkinter import filedialog
from src.scanner.scanner import Scanner

def browse_and_read_file():
    root = tk.Tk()
    root.withdraw()

    # Open a file dialog to select the file
    file_path = filedialog.askopenfilename(title="Select your code",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
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

code = browse_and_read_file()
if code:

    try:
        scanner = Scanner(code)
        tokens = scanner.tokenize()

        output_file_path = filedialog.asksaveasfilename(
            title="Save Tokens As",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )

        if output_file_path:
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                for token in tokens:
                    output_file.write(f"{token}\n")
            print(f"Tokens saved to {output_file_path}")
        else:
            print("No file selected for saving the output.")
    except Exception as e:
        print(f"Error during tokenization: {e}")
else:
    print("No code provided.")
