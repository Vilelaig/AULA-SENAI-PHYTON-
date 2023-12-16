import tkinter as tk 
from tkinter import messagebox

def create():
    item = item_entry.get()
    if item:
        item_listbox.insert(tk.END, item)
        item_entry.delete(0 ,tk.END)


def read ():
    selecte_item = item_listbox.curselection()
    if selecte_item:
        item = item_listbox.get(selecte_item)
        messagebox.showwarning('Selecionado' , f'Dados- {item}') 

def update():
    selecte_item = item_listbox.cursoselect()
    if selecte_item:
        new_item = item_entry.get()
        if new_item:
            item_listbox(tk.END, selecte_item)
            item_listbox.insert(selecte_item[0], new_item)
            item_listbox(0 , tk.END)


def delete1():
    select_item = item_listbox.curselection()
    if select_item:
        item_listbox.delete(select_item)





root = tk.Tk()  
root.title('CRUD')
root.geometry('350x150')

item_label = tk.Label(root, text='Digite o e-mail' , font=('arial, 25'), bg='blue')
item_label.pack()
item_entry = tk.Entry(root)
item_entry.pack()

btn_create = tk.Button(root, text='Salvar' , command=create)
btn_create.pack()

btn_read = tk.Button(root, text='Ler' , command=read)
btn_read.pack()

item_listbox = tk.Listbox(root, width=50, height=40)
item_listbox.pack()

btn_update = tk.Button(root, text='Atualizar' , command=update)
btn_update.pack()

btn_delete = tk.Button(root, text='Deletar' , command=delete1)
btn_delete.pack()




root.mainloop()
    