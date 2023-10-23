import os
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_files(directory, text_to_remove):
    files = os.listdir(directory)
    for file_name in files:
        if text_to_remove not in file_name:
            continue  # Skip this file if the text_to_remove is not found
        new_file_name = file_name.replace(text_to_remove, '')
        
        # Check if the new filename already exists
        counter = 1
        base_name, ext = os.path.splitext(new_file_name)
        while os.path.exists(os.path.join(directory, new_file_name)):
            new_file_name = f"{base_name} ({counter}){ext}"
            counter += 1
        
        os.rename(os.path.join(directory, file_name), os.path.join(directory, new_file_name))


def browse_directory():
    directory = filedialog.askdirectory()
    directory_label.config(text=directory)
    return directory

def start_renaming():
    directory = directory_label.cget("text")
    text_to_remove = text_entry.get()
    if not directory or not text_to_remove:
        messagebox.showerror("Error", "Please select a directory and enter text to remove.")
        return
    rename_files(directory, text_to_remove)
    messagebox.showinfo("Success", "Files renamed successfully!")
    

# Create the main window
root = tk.Tk()
root.title("File Renamer")
root.geometry("450x350")

# Create and place widgets
browse_button = tk.Button(root, text="Browse Directory", command=browse_directory)
browse_button.pack(pady=20)

directory_label = tk.Label(root, text="")
directory_label.pack(pady=10)

text_label = tk.Label(root, text="Text to remove:")
text_label.pack(pady=10)

text_entry = tk.Entry(root)
text_entry.pack(pady=10)

start_button = tk.Button(root, text="Start Renaming", command=start_renaming)
start_button.pack(pady=20)

close_button = tk.Button(root, text="Close", command=root.quit)
close_button.pack(pady=20)

root.mainloop()
