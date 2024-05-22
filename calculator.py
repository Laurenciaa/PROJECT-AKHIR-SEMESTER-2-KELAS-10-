import tkinter as tk
from ttkbootstrap import Style

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == "add":
            result.set(num1 + num2)
        elif operation == "subtract":
            result.set(num1 - num2)
        elif operation == "multiply":
            result.set(num1 * num2)
        elif operation == "divide":
            result.set("Error! Division by zero." if num2 == 0 else num1 / num2)
    except ValueError:
        result.set("Invalid input")

root = tk.Tk()
root.title("Simple Calculator")
style = Style(theme='darkly')

tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root, width=15)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root, width=15)
entry2.grid(row=1, column=1, padx=10, pady=10)

result = tk.StringVar()
tk.Label(root, text="Result:", textvariable=result, font=("Helvetica", 16)).grid(row=2, columnspan=2, padx=10, pady=10)

operations = [("Add", "add"), ("Subtract", "subtract"), ("Multiply", "multiply"), ("Divide", "divide")]
for idx, (text, op) in enumerate(operations):
    tk.Button(root, text=text, command=lambda op=op: calculate(op)).grid(row=3 + idx // 2, column=idx % 2, padx=10, pady=5)

root.mainloop()
