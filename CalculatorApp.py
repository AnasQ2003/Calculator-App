import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1, num2 = float(entry1.get()), float(entry2.get())
        if operation == "add":
            result.set(num1 + num2)
        elif operation == "subtract":
            result.set(num1 - num2)
        elif operation == "multiply":
            result.set(num1 * num2)
        elif operation == "divide":
            if num2 == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero")
            else:
                result.set(num1 / num2)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Modern Calculator")
root.geometry("450x550")
root.configure(bg="#1E1E1E")

font_style = ("Arial", 14, "bold")
button_style = {"font": ("Arial", 12, "bold"), "bg": "#3498DB", "fg": "white", "width": 10, "height": 2}

frame = tk.Frame(root, bg="#1E1E1E")
frame.pack(pady=20)

tk.Label(frame, text="Calculator", font=("Arial", 24, "bold"), fg="white", bg="#1E1E1E").pack(pady=10)

entry_style = {"font": font_style, "bg": "#ECF0F1", "fg": "black", "width": 20, "bd": 3}

tk.Label(frame, text="Enter first number:", font=font_style, fg="white", bg="#1E1E1E").pack()
entry1 = tk.Entry(frame, **entry_style)
entry1.pack(pady=5)

tk.Label(frame, text="Enter second number:", font=font_style, fg="white", bg="#1E1E1E").pack()
entry2 = tk.Entry(frame, **entry_style)
entry2.pack(pady=5)

result = tk.StringVar()
tk.Label(frame, text="Result:", font=font_style, fg="white", bg="#1E1E1E").pack()
tk.Entry(frame, textvariable=result, font=font_style, state='readonly', width=20, bd=3).pack(pady=5)

button_frame = tk.Frame(frame, bg="#1E1E1E")
button_frame.pack(pady=15)

tk.Button(button_frame, text="Add", command=lambda: calculate("add"), **button_style).grid(row=0, column=0, padx=10, pady=10)
tk.Button(button_frame, text="Subtract", command=lambda: calculate("subtract"), **button_style).grid(row=0, column=1, padx=10, pady=10)
tk.Button(button_frame, text="Multiply", command=lambda: calculate("multiply"), **button_style).grid(row=1, column=0, padx=10, pady=10)
tk.Button(button_frame, text="Divide", command=lambda: calculate("divide"), **button_style).grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Exit", command=root.quit, font=("Arial", 14, "bold"), bg="#E74C3C", fg="white", width=15, height=2).pack(pady=20)

root.mainloop()