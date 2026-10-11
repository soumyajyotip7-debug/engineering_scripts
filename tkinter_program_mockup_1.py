import tkinter as tk
from tkinter import ttk

## main window
root = tk.Tk()

## windows configuration
root.geometry("600x400")
root.title("SAW - Specimen Analysis Workflow")
root.resizable(True, True)

## header
header = tk.Frame(root, bg="#1F4E78", height=70)
header.pack(fill="x")
header.pack_propagate(False)

## SAW title at the bottom
title = tk.Label(
    header,
    text="SAW - Specimen Analysis Workflow",
    font=("Times New Roman", 22, "bold"),
    fg="white",
    bg="#1F4E78"
)
title.pack(side="bottom", padx=25, pady=15)

## menu functions
def open_instructions():
    window = tk.Toplevel(root)
    window.title("SAW - Instructions")
    window.geometry("700x450")
    window.minsize(450, 300)
    
    heading = ttk.Label(
        window,
        text="Instructions",
        font=("Times New Roman", 18, "bold")
    )

    heading.pack(anchor="w", padx=20, pady=(20, 10))
    
    instructions = (
        "Welcome to Specimen Analysis Workflow (SAW).\n\n"
        "1. Configure the required folder paths in Settings.\n"
        "2. Review the specimen definition and template information.\n"
        "3. Check the material and crack propagation settings.\n"
        "4. Validate the configuration before running an analysis.\n"
        "5. Review the generated results after execution.\n\n"
        "Note: These are initial example instructions. "
        "Replace them with the approved SAW user instructions."
    )
    text_box = tk.Text(
        window,
        wrap="word",
        font=("Times New Roman", 11),
        padx=10,
        pady=10
    )
    text_box.pack(fill="both", expand=True, padx=20, pady=(0, 20))
    text_box.insert("1.0", instructions)
    text_box.config(state="disabled")
    
def open_settings():
    window = tk.Toplevel(root)
    window.title("SAW - Settings")
    window.geometry("750x450")
    window.minsize(500, 300)
    
    heading = ttk.Label(
        window,
        text="Settings",
        font=("Times New Roman", 18, "bold")
    )
    heading.pack(anchor="w", padx=20, pady=(20, 15))
    
    settings_frame = ttk.Frame(window, padding=15)
    settings_frame.pack(fill="both", expand=True)
    
    fields = [
        ("Path to Python executable", "python.exe"),
        ("Folder containing run_saw.py", ""),
        ("Material library path", ""),
        ("Template library path", ""),
        ("Working folder", ""),
        ("Output folder", "")        
    ]
    entries = {}
    
    for row, (label_text, default_value) in enumerate(fields):
        label = ttk.Label(settings_frame, text=label_text)
        label.grid(row=row, column=0, sticky="w", padx=5, pady=8)

        entry = ttk.Entry(settings_frame, width=55)
        entry.grid(row=row, column=1, sticky="ew", padx=5, pady=8)
        entry.insert(0, default_value)

        entries[label_text] = entry

    settings_frame.columnconfigure(1, weight=1)
    
    def save_settings():
        # Demonstration only: values are not persisted to a file yet.
        print("Current SAW settings:")
        for name, entry in entries.items():
            print(f"{name}: {entry.get()}")

        tk.messagebox.showinfo(
            "Settings",
            "Settings displayed in the console.\n"
            "File saving can be added next."
        )

    save_button = ttk.Button(
        settings_frame,
        text="Save",
        command=save_settings
    )
    save_button.grid(
        row=len(fields),
        column=1,
        sticky="e",
        padx=5,
        pady=15
    )


# ---------------- HAMBURGER MENU ----------------
def show_hamburger_menu():
    menu = tk.Menu(root, tearoff=0)
    menu.add_command(
        label="Instructions",
        command=open_instructions
    )
    menu.add_command(
        label="Settings",
        command=open_settings
    )

    # Display the dropdown below the hamburger button
    x = hamburger_button.winfo_rootx()
    y = hamburger_button.winfo_rooty() + hamburger_button.winfo_height()

    menu.tk_popup(x, y)


hamburger_button = tk.Button(
    header,
    text="\u2630",
    font=("Arial", 22),
    fg="white",
    bg="#1F4E78",
    activeforeground="white",
    activebackground="#163A5A",
    relief="flat",
    borderwidth=0,
    cursor="hand2",
    command=show_hamburger_menu
)
hamburger_button.pack(side="right", padx=20, pady=10)

# Import messagebox explicitly for the Settings window
from tkinter import messagebox
tk.messagebox = messagebox

root.mainloop()