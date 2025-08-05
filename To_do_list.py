import tkinter as tk
from tkinter import messagebox
import json

# --- GUI Setup ---
root = tk.Tk()
root.title("Task List Application")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

# List to hold tasks
tasks = []
FILE_NAME = "tasks.json"

# --- Functions ---

def save_tasks():
    """Saves the current tasks list to a JSON file."""
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f)

def load_tasks():
    """Loads tasks from a JSON file into the tasks list and the GUI listbox."""
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            tasks.extend(data)
            for task in tasks:
                listbox_tasks.insert(tk.END, task)
    except FileNotFoundError:
        pass  # File doesn't exist yet, which is fine.

def add_task():
    """Adds a task from the entry field to the listbox and saves automatically."""
    task_text = entry_task.get()
    if task_text:
        tasks.append(task_text)
        listbox_tasks.insert(tk.END, task_text)
        entry_task.delete(0, tk.END)
        save_tasks()  # Auto-save after adding
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def remove_task():
    """Removes the selected task from the listbox and saves automatically."""
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
        del tasks[selected_task_index]
        save_tasks()  # Auto-save after removing
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")

def edit_task():
    """Edits the selected task with the text from the entry field and saves automatically."""
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        new_task_text = entry_task.get()
        if new_task_text:
            tasks[selected_task_index] = new_task_text
            listbox_tasks.delete(selected_task_index)
            listbox_tasks.insert(selected_task_index, new_task_text)
            entry_task.delete(0, tk.END)
            save_tasks()  # Auto-save after editing
        else:
            messagebox.showwarning("Warning", "You must enter new text to edit the task.")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to edit.")

# --- Widgets ---
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(
    frame_tasks,
    height=15,
    width=50,
    bg="white",
    fg="black",
    selectbackground="#a6a6a6",
    selectforeground="black",
    font=("Arial", 12)
)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50, font=("Arial", 12))
entry_task.pack(pady=10)

button_add_task = tk.Button(root, text="Add Task", command=add_task, font=("Arial", 12))
button_add_task.pack(pady=5, ipadx=10)

button_remove_task = tk.Button(root, text="Remove Task", command=remove_task, font=("Arial", 12))
button_remove_task.pack(pady=5, ipadx=10)

button_edit_task = tk.Button(root, text="Edit Task", command=edit_task, font=("Arial", 12))
button_edit_task.pack(pady=5, ipadx=10)

# Load tasks when the application starts
load_tasks()

# Start the main event loop
root.mainloop()