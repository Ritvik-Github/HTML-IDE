from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("HTML IDE")
root.geometry("900x700")
root.config(bg="grey")

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))

file_name_lbl = Label(root,text="File Name")
file_name_lbl.place(relx = 0.4,rely=0.1,anchor=CENTER)
file_name_entry = Entry(root)
file_name_entry.place(relx = 0.5,rely = 0.1,anchor=CENTER)
text_area = Text(root,bg="black",fg="white")
text_area.place(relx = 0.5,rely = 0.6,anchor=CENTER)
root.mainloop()