import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        w=float(w_entry.get())
        h=float(h_entry.get())
        bmi =w/(h*h)
        bmi_result_label.config(text=f"Ваш ИМТ: {bmi:.2f}")
        if bmi < 18.5:
            interpretation = "Недостаточный вес"
        elif 18.5 <= bmi<24.9:
            interpretation = "Нормальный вес"
        elif 25 <= bmi < 29.9:
            interpretation = "Избыточный вес"
        else:
            interpretation = "Ожирение"

        interpretation_result_label.config(text=f"Интерпретация: {interpretation}")
    except ValueError:
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные значения.")

root = tk.Tk()
root.title("Калькулятор ИМТ")
root.geometry("300x200")

w_label = tk.Label(root, text=" вес (кг):")
w_label.pack()

w_entry = tk.Entry(root)
w_entry.pack()

h_label = tk.Label(root, text="рост (м):")
h_label.pack()

h_entry = tk.Entry(root)
h_entry.pack()

calculate_button = tk.Button(root, text="Рассчитать ИМТ", command=calculate_bmi)
calculate_button.pack()

bmi_result_label = tk.Label(root, text="")
bmi_result_label.pack()

interpretation_result_label = tk.Label(root, text="")
interpretation_result_label.pack()

root.mainloop()