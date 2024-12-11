from PyQt5 import QtWidgets
from typing import List, Tuple

class FileManager:
    @staticmethod
    def read_code(ui) -> Tuple[str, str]:
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            caption="Open File",
            directory="",
            filter="Text Files (*.txt);;All Files (*.*)"
        )
        print(file_path)
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    result = [file_path, file.read()]
                    ui.showMessage("File read successfully.")
                    return result

            except Exception as e:
                ui.showMessage(f"Error reading file: {e}")
                return "", ""
        else:
            ui.showMessage("No file selected for reading.")
            return "", ""

    @staticmethod
    def write_tokens(ui, tokens: List) -> None:
        output_file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
                caption="Save Tokens",
                directory="",
                filter="Text Files (*.txt)"
            )

        if output_file_path:
            try:
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    for token in tokens:
                        output_file.write(f"{token}\n")

                ui.showMessage(f"Tokens saved to {output_file_path}")

            except Exception as e:
                ui.showMessage(f"Error writing tokens to file: {e}")
        else:
            ui.showMessage("No file selected for saving.")
