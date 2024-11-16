import tkinter as tk
from tkinter import filedialog, scrolledtext
from tkinter import ttk
from PIL import Image
import pytesseract
import pyperclip
import os


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class StylishConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stylish Image to Text Converter")
        self.root.geometry("900x700")
        self.root.configure(bg="#1e1e2f")

        
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

    
        self.main_frame = tk.Frame(root, bg="#2e2e3f", bd=2, relief="sunken")
        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        self.create_ui()

    def create_ui(self):
        
        title = tk.Label(
            self.main_frame,
            text="🌟 Image to Text Converter 🌟",
            font=("Helvetica", 18, "bold"),
            bg="#2e2e3f",
            fg="#f5a623"
        )
        title.pack(pady=10)

        # Image Selection - Section
        self.select_button = tk.Button(
            self.main_frame,
            text="🖼️ Select Image",
            font=("Helvetica", 14, "bold"),
            bg="#4caf50",
            fg="#ffffff",
            activebackground="#45a049",
            activeforeground="#ffffff",
            command=self.select_image
        )
        self.select_button.pack(pady=10)

        self.path_label = tk.Label(
            self.main_frame,
            text="No image selected",
            font=("Helvetica", 12),
            bg="#2e2e3f",
            fg="#d3d3d3",
            wraplength=600
        )
        self.path_label.pack()

        # Convert Image Button
        self.convert_button = tk.Button(
            self.main_frame,
            text="⚡ Convert to Text ⚡",
            font=("Helvetica", 14, "bold"),
            bg="#008cba",
            fg="#ffffff",
            activebackground="#007bb5",
            activeforeground="#ffffff",
            command=self.convert_image,
            state=tk.DISABLED
        )
        self.convert_button.pack(pady=20)

        # Text Display Area
        self.text_area = scrolledtext.ScrolledText(
            self.main_frame,
            wrap=tk.WORD,
            font=("Helvetica", 12),
            bg="#1e1e2f",
            fg="#ffffff",
            insertbackground="#ffffff",
            selectbackground="#5c5cff",
            relief="flat",
            bd=0,
            height=15
        )
        self.text_area.pack(fill=tk.BOTH, padx=20, pady=10)

        # Action Buttons
        button_frame = tk.Frame(self.main_frame, bg="#2e2e3f")
        button_frame.pack(pady=20)

        self.copy_button = tk.Button(
            button_frame,
            text="📋 Copy Text",
            font=("Helvetica", 12, "bold"),
            bg="#ffc107",
            fg="#000000",
            activebackground="#ffb300",
            activeforeground="#000000",
            command=self.copy_text,
            state=tk.DISABLED
        )
        self.copy_button.grid(row=0, column=0, padx=10)

        self.save_button = tk.Button(
            button_frame,
            text="💾 Save Text",
            font=("Helvetica", 12, "bold"),
            bg="#f44336",
            fg="#ffffff",
            activebackground="#d32f2f",
            activeforeground="#ffffff",
            command=self.save_text,
            state=tk.DISABLED
        )
        self.save_button.grid(row=0, column=1, padx=10)

        # Status Label
        self.status_label = tk.Label(
            self.main_frame,
            text="",
            font=("Helvetica", 12),
            bg="#2e2e3f",
            fg="#76ff03",
        )
        self.status_label.pack()

    def select_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.tiff")
            ]
        )
        if file_path:
            self.image_path = file_path
            self.path_label.config(text=f"Selected: {file_path}")
            self.convert_button.config(state=tk.NORMAL)
            self.status_label.config(text="")

    def convert_image(self):
        try:
            self.status_label.config(text="Converting... Please wait.", fg="#f5a623")
            self.root.update()

            
            image = Image.open(self.image_path)

            
            text = pytesseract.image_to_string(image)

            
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, text)

            
            self.save_button.config(state=tk.NORMAL)
            self.copy_button.config(state=tk.NORMAL)

            self.status_label.config(text="Conversion completed successfully!", fg="#76ff03")
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", fg="#f44336")

    def save_text(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")]
        )
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    text = self.text_area.get(1.0, tk.END)
                    file.write(text.strip())
                self.status_label.config(text="Text saved successfully!", fg="#76ff03")
            except Exception as e:
                self.status_label.config(text=f"Error saving file: {str(e)}", fg="#f44336")

    def copy_text(self):
        try:
            text = self.text_area.get(1.0, tk.END).strip()
            pyperclip.copy(text)
            self.status_label.config(text="Text copied to clipboard!", fg="#76ff03")
        except Exception as e:
            self.status_label.config(text=f"Error copying text: {str(e)}", fg="#f44336")


def main():
    root = tk.Tk()
    app = StylishConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
