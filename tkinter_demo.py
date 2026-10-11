#button widget
import tkinter as tk
# from tkinter import ttk

# create the main application window
root = tk.Tk()
root.title("Button widget example")
root.geometry("400x300")
root.configure(background='lightblue')

def say_hello():
    print("Hello, tkinter!")
    
def button_with_args(name):
    print(f"Hello, {name}!")
    
button1 = tk.Button(root, text="Click Me!", command=say_hello)
button1.pack(pady=10)

button2 = tk.Button(root, text="Styled Button", bg="black", fg="white", font=("Arial", 20, "bold"))
button2.pack(pady=10)

button3 = tk.Button(root, text="Disabled Button", state="disabled")
button3.pack(pady=10)

button4 = tk.Button(root, text="Active State Button", activebackground="red", activeforeground="yellow", command=lambda: print("Button Activated!"))
button4.pack(pady=10)

button5 = tk.Button(root, text="Greet John", command=lambda: button_with_args("John"))
button5.pack(pady=10)

root.mainloop()

