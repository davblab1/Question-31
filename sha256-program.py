"""
Завдання: Реалізувати функцію, яка виконує хешування повідомлення алгоритмом SHA-256.
Програма повинна приймати на вхід рядок та виводити його геш-значення у шістнадцятковому форматі.

Додатково:
1. CTRL + C/V/A.. працює лише з англійською розкладкою.
2. !!!Після хешування буфер обміну очищається при виході із програми. Для його збереження потрібно 
куди завгодно вставити скопійований текст, а вже потім закривати програму!!!.
"""

import hashlib
import tkinter as tk
from tkinter import messagebox

def sha256_hash(message: str) -> str:
    message_bytes = message.encode('utf-8')
    sha256 = hashlib.sha256()
    sha256.update(message_bytes)
    return sha256.hexdigest()

def hash_button_click():
    input_message = input_entry.get()
    if input_message.strip() == "":
        messagebox.showwarning("Помилка", "Будь ласка, введіть повідомлення для хешування!")
        return
    hash_result = sha256_hash(input_message)
    output_label.config(text=f"Геш-значення:\n{hash_result}")
    copy_button.config(state=tk.NORMAL)

def copy_button_click():
    hash_result = output_label.cget("text").split("\n", 1)[-1]
    root.clipboard_clear()
    root.clipboard_append(hash_result)
    root.update()
    messagebox.showinfo("Скопійовано", "Геш-значення скопійовано до буфера обміну!")

root = tk.Tk()
root.title("SHA-256 Хешування")
root.geometry("390x310")

tk.Label(root, text="Введіть повідомлення для хешування:", font=("Arial", 12)).pack(pady=10)
input_entry = tk.Entry(root, width=30, font=("Arial", 12))
input_entry.pack(pady=5)

hash_button = tk.Button(root, text="Хешувати", font=("Arial", 12), command=hash_button_click)
hash_button.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 10), wraplength=350, justify="center")
output_label.pack(pady=10)

copy_button = tk.Button(root, text="Копіювати геш", font=("Arial", 12), command=copy_button_click, state=tk.DISABLED)
copy_button.pack(pady=10)

root.mainloop()