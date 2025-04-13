import tkinter as tk
from tkinter import filedialog, messagebox
from parser import read_log_file, filter_log_lines, count_matches, export_logs_to_csv
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

def highlight_keyword(keyword):
    text_area.tag_remove("highlight", "1.0", tk.END)
    if not keyword:
        return
    start = "1.0"
    while True:
        pos = text_area.search(keyword, start, stopindex=tk.END, nocase=True)
        if not pos:
            break
        end = f"{pos}+{len(keyword)}c"
        text_area.tag_add("highlight", pos, end)
        start = end
    text_area.tag_config("highlight", background="yellow", foreground="black")

def filter_logs():
    keyword = keyword_entry.get().strip()
    if not keyword:
        result_label.config(text="Please enter a keyword to filter.", fg="red")
        return
    filtered = filter_log_lines(log_lines, keyword)
    display_logs(filtered)
    highlight_keyword(keyword)
    match_count = count_matches(log_lines, keyword)
    result_label.config(text=f"{match_count} matches found for '{keyword}'", fg="blue")

def get_displayed_lines():
    content = text_area.get("1.0", tk.END).strip()
    return [line for line in content.splitlines() if line.strip() and not line.startswith("-")]

def export_logs():
    displayed = get_displayed_lines()
    if not displayed:
        messagebox.showerror("Error", "No log data to export.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return

    try:
        export_logs_to_csv(displayed, file_path)
        messagebox.showinfo("Success", f"Logs exported to {file_path}")
    except Exception as e:
        messagebox.showerror("Export Failed", str(e))
        
def export_logs_to_txt():
    displayed = get_displayed_lines()
    if not displayed:
        messagebox.showerror("Error", "No log data to export.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not file_path:
        return

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(displayed))
        messagebox.showinfo("Success", f"Logs exported to {file_path}")
    except Exception as e:
        messagebox.showerror("Export Failed", str(e))

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
keyword_entry.insert(0, "Filter logs...")
keyword_entry.config(fg="grey")

def on_entry_click(event):
    if keyword_entry.get() == "Filter logs...":
        keyword_entry.delete(0, tk.END)
        keyword_entry.config(fg="black")

keyword_entry.bind("<FocusIn>", on_entry_click)

filter_btn = tk.Button(root, text="Filter Logs", command=filter_logs)
filter_btn.pack(pady=5)

result_label = tk.Label(root, text="", fg="blue", font=("Arial", 10))
result_label.pack(pady=5)

text_area = tk.Text(root, wrap='word', font=("Courier", 10))
text_area.pack(expand=True, fill='both', padx=10, pady=10)

export_frame = tk.Frame(root)
export_frame.pack(pady=5)

export_btn = tk.Button(export_frame, text="Export to CSV", command=export_logs)
export_btn.pack(side=tk.LEFT, padx=5)

export_txt_btn = tk.Button(export_frame, text="Export to TXT", command=export_logs_to_txt)
export_txt_btn.pack(side=tk.LEFT, padx=5)

log_lines = []  
root.mainloop()
