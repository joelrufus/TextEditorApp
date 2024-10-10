import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess

def run_cpp_program(args):
    try:
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)

def create_file():
    filename = entry_filename.get()
    content = text_content.get("1.0", tk.END).strip()
    
    output = run_cpp_program(["./text_editor", "create", filename, content])
    messagebox.showinfo("Result", output)

def read_file():
    filename = entry_filename.get()
    
    output = run_cpp_program(["./text_editor", "read", filename])
    if "does not exist" in output:
        messagebox.showerror("Error", output)
    else:
        text_content.delete("1.0", tk.END)
        text_content.insert(tk.END, output)

def update_file():
    filename = entry_filename.get()
    content = text_content.get("1.0", tk.END).strip()
    
    output = run_cpp_program(["./text_editor", "update", filename, content])
    messagebox.showinfo("Result", output)

def delete_file():
    filename = entry_filename.get()
    
    output = run_cpp_program(["./text_editor", "delete", filename])
    messagebox.showinfo("Result", output)

def search_word():
    filename = entry_filename.get()
    word = entry_search_word.get()
    
    output = run_cpp_program(["./text_editor", "search", filename, word])
    messagebox.showinfo("Search Result", output)

def file_stats():
    filename = entry_filename.get()
    
    output = run_cpp_program(["./text_editor", "stats", filename])
    messagebox.showinfo("File Statistics", output)

root = tk.Tk()
root.title("Text Editor - Joel Rufus")
root.geometry("600x600")
root.resizable(False, False)

style = ttk.Style(root)
style.theme_use('clam')

bg_color = "#1e1f26"     
fg_color = "#FFFFFF"     
button_color = "#00BFFF" 
search_color = "#FF4500" 

root.configure(background=bg_color)

style.configure("TLabel", background=bg_color, foreground=fg_color, font=('Helvetica', 12))
style.configure("TButton", foreground=fg_color, background=button_color, font=('Helvetica', 10, 'bold'), padding=6)
style.map("TButton", background=[("active", "#4682B4")])  # Button color on hover

main_frame = ttk.Frame(root, padding="10 10 10 10", style="TFrame")
main_frame.pack(fill=tk.BOTH, expand=True)


filename_frame = ttk.Frame(main_frame, style="TFrame")
filename_frame.pack(fill=tk.X, pady=5)

label_filename = ttk.Label(filename_frame, text="File Name:", style="TLabel")
label_filename.pack(side=tk.LEFT)

entry_filename = ttk.Entry(filename_frame, width=40)
entry_filename.pack(side=tk.LEFT, padx=5)

label_content = ttk.Label(main_frame, text="File Content:", style="TLabel")
label_content.pack(anchor=tk.W, pady=5)

text_content = tk.Text(main_frame, height=10, width=70, background="#2F4F4F", foreground=fg_color, font=('Helvetica', 12))
text_content.pack(fill=tk.BOTH, expand=True)

button_frame = ttk.Frame(main_frame, style="TFrame")
button_frame.pack(fill=tk.X, pady=10)

btn_create = ttk.Button(button_frame, text="Create File", command=create_file)
btn_create.pack(side=tk.LEFT, padx=5)

btn_read = ttk.Button(button_frame, text="Read File", command=read_file)
btn_read.pack(side=tk.LEFT, padx=5)

btn_update = ttk.Button(button_frame, text="Update File", command=update_file)
btn_update.pack(side=tk.LEFT, padx=5)

btn_delete = ttk.Button(button_frame, text="Delete File", command=delete_file)
btn_delete.pack(side=tk.LEFT, padx=5)

search_frame = ttk.Frame(main_frame, style="TFrame")
search_frame.pack(fill=tk.X, pady=5)

label_search_word = ttk.Label(search_frame, text="Word to Search:", style="TLabel")
label_search_word.pack(side=tk.LEFT)

entry_search_word = ttk.Entry(search_frame, width=30)
entry_search_word.pack(side=tk.LEFT, padx=5)

btn_search = ttk.Button(search_frame, text="Search Word in File", command=search_word)
btn_search.pack(side=tk.LEFT, padx=5)

style.configure("Search.TButton", foreground=fg_color, background=search_color, font=('Helvetica', 10, 'bold'), padding=6)
style.map("Search.TButton", background=[("active", "#FF6347")])  # Button hover color

btn_search.config(style="Search.TButton")

btn_stats = ttk.Button(main_frame, text="Show File Statistics", command=file_stats)
btn_stats.pack(pady=10)

root.mainloop()
