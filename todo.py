import tkinter as tk

def add_item():
    item = input_field.get()
    if item:
        list_box.insert("end", item)
        input_field.delete(0, "end")

def check_off():
    selected = list_box.curselection()
    for index in selected:
        list_box.itemconfig(index, {'fg': 'gray'})

root = tk.Tk()
root.title("To-Do List")

input_field = tk.Entry(root)
input_field.pack()

add_button = tk.Button(root, text="Add", command=add_item)
add_button.pack()

list_box = tk.Listbox(root)
list_box.pack()

check_off_button = tk.Button(root, text="Check off", command=check_off)
check_off_button.pack()

root.mainloop()
