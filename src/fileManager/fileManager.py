from tkinter import filedialog, messagebox
from typing import List, Optional

class FileManager:
    @staticmethod
    def read_code() -> Optional[str]:
        file_path = filedialog.askopenfilename(title="Select your code",
                                               filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()  # Read the file content
                    return content

            except Exception as e:
                messagebox.showerror("File Error", f"Error reading file: {e}")
                return None
        else:
            messagebox.showwarning("File Selection", "No file selected.")
            return None

    @staticmethod
    def write_tokens(tokens: List) -> None:
        output_file_path = filedialog.asksaveasfilename(
            title="Save Tokens As",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )

        if output_file_path:
            try:
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    for token in tokens:
                        output_file.write(f"{token}\n")

                messagebox.showinfo("Success", f"Tokens saved to {output_file_path}")

            except Exception as e:
                messagebox.showerror("File Error", f"Error writing tokens to file: {e}")
        else:
            messagebox.showwarning("Save Tokens", "No file selected for saving.")

