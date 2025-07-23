import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from datetime import datetime
import os

# Initialize Window
root = tk.Tk()
root.title("My Personal Diary")
root.geometry("700x600")
root.config(bg="#f8f1f1")

# Title Label
title_label = tk.Label(root, text="My Personal Diary", font=("Georgia", 20, "bold"), fg="#333", bg="#f8f1f1")
title_label.pack(pady=10)

# Scrollable Text Area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Calibri", 13), bg="#fffdf7", fg="#2e2e2e", relief=tk.SOLID, bd=2)
text_area.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Save Function
def save_entry():
    content = text_area.get("1.0", tk.END).strip()
    if not content:
        messagebox.showerror("Empty Entry", "Diary entry is empty.")
        return
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"Diary_{date_str}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    messagebox.showinfo("Saved", f"Diary saved as '{filename}'")

# Load Function
def load_entry():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path and os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)

# Bottom Frame for Buttons
button_frame = tk.Frame(root, bg="#f8f1f1")
button_frame.pack(pady=10)

# Stylish Buttons
save_btn = tk.Button(button_frame, text=" Save Entry", font=("Arial", 12, "bold"), command=save_entry, bg="#4CAF50", fg="white", padx=20, pady=5, relief=tk.FLAT, cursor="hand2")
save_btn.pack(side=tk.LEFT, padx=15)

load_btn = tk.Button(button_frame, text=" Load Entry", font=("Arial", 12, "bold"), command=load_entry, bg="#2196F3", fg="white", padx=20, pady=5, relief=tk.FLAT, cursor="hand2")
load_btn.pack(side=tk.LEFT, padx=15)

# Start GUI Loop
root.mainloop()