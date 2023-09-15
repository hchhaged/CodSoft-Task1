import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def update_task():
    try:
        index = listbox_tasks.curselection()[0]
        task = entry_task.get()
        if task:
            listbox_tasks.delete(index)
            listbox_tasks.insert(index, task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

def save_tasks():
    tasks = listbox_tasks.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                listbox_tasks.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, height=15, width=50, bg="lightgray", selectbackground="yellow")
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=5)

button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.pack(side=tk.LEFT, padx=5)

button_remove_task = tk.Button(root, text="Remove Task", command=remove_task)
button_remove_task.pack(side=tk.LEFT, padx=5)

button_update_task = tk.Button(root, text="Update Task", command=update_task)
button_update_task.pack(side=tk.LEFT, padx=5)

button_save_tasks = tk.Button(root, text="Save Tasks", command=save_tasks)
button_save_tasks.pack(side=tk.LEFT, padx=5)

load_tasks()

root.mainloop()