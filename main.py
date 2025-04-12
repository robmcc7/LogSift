import tkinter as tk
from tkinter import filedialog, messagebox
from parser import read_log_file, filter_log_lines, count_matches
import os

log_lines = []

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Log files", "*.log *.txt")])
    if file_path:
        global log_lines
        log_lines = read_log_file(file_path)
        display_logs(log_lines)
        file_label.config(text=os.path.basename(file_path))

def display_logs(lines):
    text_area.delete("1.0", tk.END)
    for line in lines:
        text_area.insert(tk.END, line.strip() + "\n")
        text_area.insert(tk.END, "-" * 60 + "\n")

def filter_logs():
    keyword = keyword_entry.get().strip()
    if not keyword:
        result_label.config(text="Please enter a keyword to filter.", fg="red")
        return
    filtered = filter_log_lines(log_lines, keyword)
    display_logs(filtered)
    match_count = count_matches(log_lines, keyword)
    result_label.config(text=f"{match_count} matches found for '{keyword}'", fg="blue")

# --- GUI SETUP ---
root = tk.Tk()
root.title("LogSift: Your Favorite Log Tool!")
root.geometry("800x600")

top_frame = tk.Frame(root)
top_frame.pack(pady=10)

open_btn = tk.Button(top_frame, text="Open Log File", command=open_file)
open_btn.pack(side=tk.LEFT, padx=5)

file_label = tk.Label(top_frame, text="No file selected")
file_label.pack(side=tk.LEFT)

keyword_entry = tk.Entry(root, width=30)
keyword_entry.pack(pady=5)
keyword_entry.insert(0, "Enter keyword")

filter_btn = tk.Button(root, text="Filter Logs", command=filter_logs)
filter_btn.pack(pady=5)

result_label = tk.Label(root, text="", fg="blue", font=("Arial", 10))
result_label.pack(pady=5)

text_area = tk.Text(root, wrap='word', font=("Courier", 10))
text_area.pack(expand=True, fill='both', padx=10, pady=10)

log_lines = []  
root.mainloop()
