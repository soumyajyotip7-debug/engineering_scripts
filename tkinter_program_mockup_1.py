
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("SAW - Specimen Analysis Workflow")
root.geometry("1000x650")
root.minsize(600, 400)
root.resizable(True, True)

# ---------------- HEADER ----------------
header = tk.Frame(root, bg="#1F4E78", height=70)
header.pack(fill="x")
header.pack_propagate(False)

title = tk.Label(
    header,
    text="SAW",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#1F4E78"
)
title.pack(side="left", padx=25, pady=10)

# ---------------- SECONDARY WINDOWS ----------------
def open_instructions():
    window = tk.Toplevel(root)
    window.title("SAW - Instructions")
    window.geometry("650x400")

    ttk.Label(
        window, text="Instructions",
        font=("Arial", 18, "bold")
    ).pack(anchor="w", padx=20, pady=15)

    text = tk.Text(window, wrap="word", font=("Arial", 11))
    text.pack(fill="both", expand=True, padx=20, pady=(0, 20))
    text.insert(
        "1.0",
        "Welcome to SAW.\n\n"
        "1. Configure the required paths in Settings.\n"
        "2. Review the specimen and template information.\n"
        "3. Validate the configuration before analysis.\n"
        "4. Review the generated results.\n\n"
        "Replace these examples with the approved SAW instructions."
    )
    text.config(state="disabled")


def open_settings():
    window = tk.Toplevel(root)
    window.title("SAW - Settings")
    window.geometry("700x400")

    ttk.Label(
        window, text="Settings",
        font=("Arial", 18, "bold")
    ).pack(anchor="w", padx=20, pady=15)

    frame = ttk.Frame(window, padding=10)
    frame.pack(fill="both", expand=True)

    fields = [
        "Path to Python executable",
        "Folder containing run_saw.py",
        "Material library path",
        "Template library path",
        "Working folder",
        "Output folder"
    ]

    entries = {}

    for i, field in enumerate(fields):
        ttk.Label(frame, text=field).grid(
            row=i, column=0, sticky="w", padx=5, pady=7
        )
        entry = ttk.Entry(frame, width=45)
        entry.grid(row=i, column=1, sticky="ew", padx=5, pady=7)
        entries[field] = entry

    frame.columnconfigure(1, weight=1)

    def save_settings():
        for field, entry in entries.items():
            print(f"{field}: {entry.get()}")
        messagebox.showinfo(
            "Settings",
            "Values printed in the Python console.\n"
            "File saving is not implemented yet.",
            parent=window
        )

    ttk.Button(
        frame, text="Save", command=save_settings
    ).grid(row=len(fields), column=1, sticky="e", pady=12)


# ---------------- HAMBURGER DROPDOWN ----------------
def show_hamburger_menu(event=None):
    menu = tk.Menu(root, tearoff=0)
    menu.add_command(label="Instructions", command=open_instructions)
    menu.add_command(label="Settings", command=open_settings)

    try:
        menu.tk_popup(
            hamburger_button.winfo_rootx(),
            hamburger_button.winfo_rooty()
            + hamburger_button.winfo_height()
        )
    finally:
        menu.grab_release()


hamburger_button = tk.Button(
    header,
    text="\u2630  MENU",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#163A5A",
    activeforeground="white",
    activebackground="#285D85",
    relief="raised",
    bd=2,
    padx=12,
    pady=5,
    cursor="hand2",
    command=show_hamburger_menu
)
hamburger_button.pack(side="right", padx=15, pady=12)

# ---------------- MAIN CONTENT ----------------
main_frame = tk.Frame(root, bg="#F2F2F2")
main_frame.pack(fill="both", expand=True)

ttk.Label(
    main_frame,
    text="Specimen Analysis Workflow (SAW)",
    font=("Arial", 16)
).pack(pady=30)

root.mainloop()
