import tkinter as tk
from tkinter import ttk

def on_dropdown_selected(event):
    selected_item = dropdown_var.get()
    result_label.config(text=f"Selected: {selected_item}")

root = tk.Tk()
root.title("Simple Dropdown Menu")

options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5']
dropdown_var = tk.StringVar(value=options[0])

dropdown_label = ttk.Label(root, text="Select an option:")
dropdown_label.pack(padx=10, pady=5)

dropdown = ttk.Combobox(root, textvariable=dropdown_var, values=options)
dropdown.bind("<<ComboboxSelected>>", on_dropdown_selected)
dropdown.pack(padx=10, pady=5)

result_label = ttk.Label(root, text="")
result_label.pack(padx=10, pady=5)

root.mainloop()