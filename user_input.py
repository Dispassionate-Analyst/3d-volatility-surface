
import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk


def get_user_input():
    root = tk.Tk()
    root.withdraw()

    symbol = simpledialog.askstring("Input", "Enter the ticker symbol:")

    # Create a new window for dropdowns
    dropdown_window = tk.Toplevel(root)
    dropdown_window.title("Select Options")

    # Option Type Dropdown
    tk.Label(dropdown_window, text="Select Option Type:").grid(row=0, column=0)
    option_type_var = tk.StringVar(dropdown_window)
    option_type_dropdown = ttk.Combobox(dropdown_window, textvariable=option_type_var)
    option_type_dropdown['values'] = ("Calls", "Puts")
    option_type_dropdown.grid(row=0, column=1)
    option_type_dropdown.current(0)  # Set default value

    # Log Scale Dropdown
    tk.Label(dropdown_window, text="Use Log Scale:").grid(row=1, column=0)
    use_log_var = tk.StringVar(dropdown_window)
    use_log_dropdown = ttk.Combobox(dropdown_window, textvariable=use_log_var)
    use_log_dropdown['values'] = ("No", "Yes")
    use_log_dropdown.grid(row=1, column=1)
    use_log_dropdown.current(0)  # Set default value

    def submit():
        dropdown_window.quit()
        dropdown_window.destroy()

    tk.Button(dropdown_window, text="Submit", command=submit).grid(row=2, columnspan=2)

    dropdown_window.mainloop()

    option_type = option_type_var.get()
    use_log_input = use_log_var.get()

    use_log = True if use_log_input == 'yes' else False

    return symbol, option_type, use_log
