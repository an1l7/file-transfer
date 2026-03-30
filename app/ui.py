import os
import tkinter as tk
from tkinter import filedialog
from .server import file_list
from .utils import get_local_ip

def start_ui():
    root = tk.Tk()
    root.title("Wireless Transfer Server")

    def add_file():
        filenames = filedialog.askopenfilenames()
        for path in filenames:
            file_list.append({"name": os.path.basename(path), "path": path})
        update_list()

    def update_list():
        listbox.delete(0, tk.END)
        for f in file_list:
            listbox.insert(tk.END, f["name"])

    def remove_selected():
        sel = listbox.curselection()
        if sel:
            del file_list[sel[0]]
            update_list()

    def remove_all():
        file_list.clear()
        update_list()

    def copy_url():
        url = f"http://{get_local_ip()}:5000"
        root.clipboard_clear()
        root.clipboard_append(url)

    def exit_app():
        root.destroy()
        os._exit(0)

    listbox = tk.Listbox(root, width=50)
    listbox.pack(padx=10, pady=10)

    tk.Button(root, text="Add File(s)", command=add_file).pack(pady=5)
    tk.Button(root, text="Remove Selected", command=remove_selected).pack(pady=5)
    tk.Button(root, text="Remove All", command=remove_all).pack(pady=5)
    tk.Button(root, text="Copy URL", command=copy_url).pack(pady=5)
    tk.Button(root, text="EXIT", command=exit_app).pack(pady=5)

    label = tk.Label(root, text=f"Server Running\nhttp://{get_local_ip()}:5000")
    label.pack(pady=10)

    root.mainloop()