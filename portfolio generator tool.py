import tkinter as tk
from tkinter import messagebox

def generate_portfolio():
    name = name_entry.get()
    bio = bio_entry.get("1.0", tk.END).strip()
    skills = skills_entry.get("1.0", tk.END).strip().split('\n')
    projects = projects_entry.get("1.0", tk.END).strip().split('\n')

    if not name or not bio:
        messagebox.showerror("Input Error", "Name and Bio are required.")
        return

    output = f"📄 PORTFOLIO\n\n Name: {name}\n\n Bio:\n{bio}\n\n🛠 Skills:\n"
    output += '\n'.join([f"• {skill}" for skill in skills if skill]) + "\n\n Projects:\n"
    output += '\n'.join([f"• {proj}" for proj in projects if proj])

    output_box.config(state='normal')
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, output)
    output_box.config(state='disabled')

# GUI Setup
root = tk.Tk()
root.title("Portfolio Generator")
root.geometry("600x600")
root.configure(bg="#f7f9fc")

tk.Label(root, text="Portfolio Generator Tool", font=("Helvetica", 18, "bold"), bg="#f7f9fc", fg="#2c3e50").pack(pady=10)

frame = tk.Frame(root, bg="#f7f9fc")
frame.pack(pady=5)

tk.Label(frame, text=" Name:", bg="#f7f9fc").grid(row=0, column=0, sticky='e')
name_entry = tk.Entry(frame, width=40)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text=" Bio:", bg="#f7f9fc").grid(row=1, column=0, sticky='ne')
bio_entry = tk.Text(frame, width=30, height=3)
bio_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text=" Skills (one per line):", bg="#f7f9fc").grid(row=2, column=0, sticky='ne')
skills_entry = tk.Text(frame, width=30, height=4)
skills_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text=" Projects (one per line):", bg="#f7f9fc").grid(row=3, column=0, sticky='ne')
projects_entry = tk.Text(frame, width=30, height=4)
projects_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text=" Generate Portfolio", command=generate_portfolio, bg="#3498db", fg="white", font=("Arial", 12)).pack(pady=10)

output_box = tk.Text(root, height=15, width=70, font=("Courier", 10), bd=2, relief="groove", bg="#ffffff")
output_box.pack(pady=10)
output_box.config(state='disabled')

root.mainloop()


