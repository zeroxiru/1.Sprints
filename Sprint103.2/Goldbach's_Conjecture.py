import openpyxl
import tkinter as tk
from tkinter import filedialog, messagebox


def detect_formula_errors():
    # Open file dialog to select Excel file
    filepath = filedialog.askopenfilename(title="Select Excel file", filetypes=[("Excel files", "*.xlsx")])

    try:
        # Load the workbook
        workbook = openpyxl.load_workbook(filepath)

        # Get the active sheet
        sheet = workbook._active

        # Iterate over each cell in the sheet
        for row in sheet.iter_rows():
            for cell in row:
                # Check if the cell contains a formula
                if cell.data_type == 'f':
                    formula = cell.value

                    # Try evaluating the formula
                    try:
                        eval(formula)
                    except Exception as e:
                        # Display error message for invalid formula
                        messagebox.showerror("Formula Error", f"Invalid formula in cell {cell.coordinate}: {str(e)}")

        # Close the workbook
        workbook.close()

        messagebox.showinfo("Formula Check", "Formula check completed. No errors found.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Create the GUI window
window = tk.Tk()
window.title("Excel Formula Error Detector")

# Create a button to trigger the formula error detection
button = tk.Button(window, text="Detect Formula Errors", command=detect_formula_errors)
button.pack(pady=10)

# Run the GUI event loop
window.mainloop()
