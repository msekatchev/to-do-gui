import tkinter as tk

# Define an empty list to store the items and their check-off status
items = []

def add_item():
    item = input_field.get()
    if item:
        # Append the new item to the `items` list with an initial check-off status of `False`
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
            # Update the check-off status of the selected item in the `items` list
            items[index] = (items[index][0], "False")

def delete_item():
    selected = list_box.curselection()
    for index in selected:
        list_box.delete(index)
        items.pop(index)
    list_box.selection_set(0)

def save_items():
    with open('todo.txt', 'w') as f:
        # Write the contents of the `items` list to the file in the format "item,check-off status\n"
        for item in items:
            f.write(f"{item[0]},{item[1]}\n")

def load_items():
    try:
        with open('todo.txt', 'r') as f:
            # Read the contents of the file and update the `items` list with the saved items and their check-off status
            for line in f:
                item, check_off = line.strip().split(',')
                items.append((item, check_off))
                list_box.insert("end", item)
                if check_off == "False":						#
                	list_box.itemconfig("end", {'fg': 'gray'})	#
    except FileNotFoundError:
        pass

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
# Load the contents of the file to restore the previous state of the to-do list
load_items()
root.geometry("300x600") 
root.mainloop()

