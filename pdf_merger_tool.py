import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger Tool")
        self.root.geometry("400x300")
        self.pdf_files = []

        self.label = tk.Label(root, text="Select PDF files to merge", font=("Arial", 14))
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Add PDFs", command=self.add_pdfs)
        self.add_button.pack(pady=5)

        self.merge_button = tk.Button(root, text="Merge and Save", command=self.merge_pdfs)
        self.merge_button.pack(pady=5)

        self.clear_button = tk.Button(root, text="Clear List", command=self.clear_list)
        self.clear_button.pack(pady=5)

    def add_pdfs(self):
        files = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF Files", "*.pdf")])
        for file in files:
            if file not in self.pdf_files:
                self.pdf_files.append(file)
                self.listbox.insert(tk.END, file)

    def clear_list(self):
        self.pdf_files = []
        self.listbox.delete(0, tk.END)

    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showerror("No files", "Please add at least two PDF files.")
            return

        merger = PdfMerger()
        for pdf in self.pdf_files:
            merger.append(pdf)

        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if save_path:
            merger.write(save_path)
            merger.close()
            messagebox.showinfo("Success", f"PDFs merged and saved as:\n{save_path}")
            self.clear_list()
        else:
            messagebox.showwarning("Cancelled", "Save cancelled. File not saved.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
