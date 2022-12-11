import tkinter as tk
import pyshorteners as ps

root=tk.Tk()

root.geometry("600x400")

name_var=tk.StringVar()

def submit():
	name=name_var.get()
	u = ps.Shortener().tinyurl.short(name)
	label = Label(root, text =u).pack()
	name_var.set("")
	

name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))


name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

sub_btn=tk.Button(root,text = 'Submit',command = submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
sub_btn.grid(row=2,column=1)
root.mainloop()
