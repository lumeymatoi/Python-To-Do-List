import tkinter as tk
from asyncio import tasks

tasks = []

def add_task():
    new_task = entry.get()

    if new_task:
        tasks.append(new_task)
        entry.delete(0, tk.END)
        refresh_list()

def remove_task():
    chosen = list.curselection()

    if chosen:
        index = chosen[0]
        tasks.pop(index)
        refresh_list()

def refresh_list():
    list.delete(0, tk.END)

    for i, task in enumerate(tasks):
        list.insert(tk.END, f"{i + 1}. {task}")

root = tk.Tk()
root.title("My To-Do List")
root.geometry("500x500")
root.configure(bg="black")

title = tk.Label(root, text="---Welcome to Your To-Do list !---", font=("Arial", 18), bg="black", fg="white")

title.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 16), width=30)

entry.pack(pady=10)

button_add = tk.Button(root,text="Add Task",  command=add_task, font=("Arial", 14))

button_add.pack(pady=5)
list = tk.Listbox(root,font=("Arial", 16),width=35,height=10)

list.pack(pady=20)

remove_button = tk.Button(
    root, text="Remove Task",command=remove_task,font=("Arial", 14))

remove_button.pack(pady=5)


root.mainloop()
