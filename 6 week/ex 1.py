import tkinter as tk
from tkinter import messagebox

def evaluate_expression():
    try:
        result = eval(entry.get())
        output_label.config(text=f"Результат: {result}")
    except Exception as e:
        messagebox.showerror("Ошибка", "Некорректное выражение")
root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

calculate_button = tk.Button(root, text="Вычислить", command=evaluate_expression)
calculate_button.pack(pady=5)


output_label = tk.Label(root, text="Результат: ")
output_label.pack(pady=10)

root.mainloop()
