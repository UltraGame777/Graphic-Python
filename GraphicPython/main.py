from tkinter import *
from tkinter import ttk, filedialog, messagebox

def open_file():
    
    file_path = filedialog.askopenfilename(
        title="Choose a Python File",
        filetypes=[("Python Files", "*.py")]
    )
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                editor.delete("1.0", END)
                editor.insert("1.0", content)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file\n{e}")

def save_file():
    
    filepath = filedialog.asksaveasfilename(
        defaultextension=".py",
        filetypes=[("Python Files", "*.py")]
    )
    if filepath:
        try:
            content = editor.get("1.0", END)
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(content)
            messagebox.showinfo("Info", "File is Saved")
        except Exception as e:
            messagebox.showerror("Error", f"Save error: {e}")

def base_text():
    editor.delete("1.0", END)
    code = "from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title('My App')\nroot.geometry('1080x720')\n\nroot.mainloop()"
    editor.insert("1.0", code)

def add_btn():
    code_with_btn = "from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title('My App')\nroot.geometry('1080x720')\n\nmy_btn = ttk.Button(text='My Button')\nmy_btn.pack()\n\nroot.mainloop()"
    editor.delete("1.0", END)
    editor.insert("1.0", code_with_btn)
def open_functions():
    new_window = Toplevel(root)
    new_window.title("Functions List")
    new_window.geometry("800x400")
    icon = PhotoImage(file="func_icon.png")
    new_window.iconphoto(FALSE, icon)
    tree = ttk.Treeview(show="tree")
    tree.pack(expand=1, fill=BOTH)

    tree.insert("", END, iid=1, text="Fetch An Element", open=False)
    tree.insert("", END, iid=2, text="Code Functions", open=False)

    tree.insert(1, index=END, text="entry.get")
    tree.insert(2, index=END, text="def delete_code():")
def add_entry():
    code_with_entry = "from tkinter import *\nfrom tkinter import ttk\n\nroot = Tk()\nroot.title('My App')\nroot.geometry('1080x720')\n\nmy_ent = ttk.Entry\nmy_ent.pack()\n\n\nroot.mainloop()"
    editor.delete("1.0", END)
    editor.insert("1.0", code_with_entry)
def add_ent_btn():
    code_with_entry_n_btn = "from tkinter import *\nfrom tkinter import ttk\nroot = Tk()\nroot.title('My App')\nroot.geometry('1080x720')\n\nmy_ent = ttk.Entry\nmy_ent.pack()\n\nmy_btn = ttk.Button(text='Button')\nmy_btn.pack()\n\n\nroot.mainloop()"
    editor.delete("1.0", END)
    editor.insert("1.0", code_with_entry_n_btn)

root = Tk()
root.title("Graphic Python")
root.geometry("1080x720")
icon = PhotoImage(file="logo.png")
root.iconphoto(FALSE, icon)
root.option_add("*tearOff", FALSE)

main_menu = Menu(root)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(main_menu, tearoff=0)
edit_menu.add_command(label="Functions", command=open_functions)

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=main_menu)

toolbar = Frame(root)
toolbar.pack(side=TOP, fill=X, padx=5, pady=5)

ttk.Button(toolbar, text="Add Base", command=base_text).pack(side=LEFT, padx=2)
ttk.Button(toolbar, text="Add Button", command=add_btn).pack(side=LEFT, padx=2)
ttk.Button(toolbar, text="Add Entry", command=add_entry).pack(side=LEFT, padx=2)
ttk.Button(toolbar, text="Add Ent/Btn", command=add_ent_btn).pack(side=LEFT, padx=2)

editor = Text(root, font=("Lucida Console", 15), undo=True)
editor.pack(fill=BOTH, expand=1, padx=5, pady=5)

root.mainloop()
