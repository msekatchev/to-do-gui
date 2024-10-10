import os
import subprocess
import tkinter as tk

# Define an empty list to store the items and their check-off status
items = []

def add_item():
    item = input_field.get()
    if item:
        items.append((item, "False"))
        list_box.insert("end", item)
        input_field.delete(0, "end")

def check_off():
    selected = list_box.curselection()
    for index in selected:
        if items[index][1] == "False":
            list_box.itemconfig(index, {'fg': 'black'})
            items[index] = (items[index][0], "True")
        else:
            list_box.itemconfig(index, {'fg': 'gray'})
            items[index] = (items[index][0], "False")

def delete_item():
    selected = list_box.curselection()
    for index in selected:
        list_box.delete(index)
        items.pop(index)
    list_box.selection_set(0)

def save_items():
    with open('todo.txt', 'w') as f:
        for item in items:
            f.write(f"{item[0]},{item[1]}\n")
    push_to_github()

def load_items():
    try:
        with open('todo.txt', 'r') as f:
            for line in f:
                item, check_off = line.strip().split(',')
                items.append((item, check_off))
                list_box.insert("end", item)
                if check_off == "False":
                    list_box.itemconfig("end", {'fg': 'gray'})
    except FileNotFoundError:
        pass

def push_to_github():
    try:
        # Load the GitHub token from the file
        with open('github-code.txt', 'r') as f:
            github_token = f.read().strip()

        # GitHub repository URL with token authentication
        github_url = f"https://{github_token}:x-oauth-basic@github.com/msekatchev/to-do-gui.git"

        # Add the changes
        subprocess.run(["git", "add", "todo.txt"], check=True)
        # Commit the changes
        subprocess.run(["git", "commit", "-m", "Update to-do list"], check=True)
        # Push the changes using the token for authentication
        subprocess.run(["git", "push", github_url, "main"], check=True)
        
        print("Pushed to GitHub successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error pushing to GitHub: {e}")
    except FileNotFoundError:
        print("GitHub token file not found.")

root = tk.Tk()
root.title("To-Do List")

input_frame = tk.Frame(root)
input_frame.pack(fill="x", padx=10, pady=10)

input_field = tk.Entry(input_frame)
input_field.pack(side="left", expand=True, fill="x")

add_button = tk.Button(input_frame, text="Add", command=add_item)
add_button.pack(side="left", padx=(5, 0))

list_box = tk.Listbox(root)
list_box.pack(fill="both", expand=True, padx=10, pady=(0, 10))

scrollbar = tk.Scrollbar(list_box)
scrollbar.pack(side="right", fill="y")

list_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_box.yview)

check_off_button = tk.Button(root, text="Check off", command=check_off)
check_off_button.pack(side="left", padx=(10, 0))

delete_button = tk.Button(root, text="Delete", command=delete_item)
delete_button.pack(side="left", padx=(5, 0))

save_button = tk.Button(root, text="Save", command=save_items)
save_button.pack(side="left", padx=(5, 0))

load_items()
root.geometry("300x600") 
root.mainloop()

