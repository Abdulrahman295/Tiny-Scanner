import tkinter as tk
from tkinter import messagebox
from src.scanner.scanner import Scanner
from src.fileManager.fileManager import FileManager

root = tk.Tk()
root.withdraw()

try:
    code = FileManager.read_code()
    if code:
        scanner = Scanner(code)
        tokens = scanner.tokenize()
        FileManager.write_tokens(tokens)

except Exception as e:
    messagebox.showerror("Tokenization Error", f"Error during processing: {e}")