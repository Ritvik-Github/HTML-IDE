from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import messagebox
import os
root = Tk()
root.title("HTML IDE")
root.geometry("900x700")
root.config(bg="grey")

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

file_name_lbl = Label(root,text="File Name")
file_name_lbl.place(relx = 0.4,rely=0.1,anchor=CENTER)
file_name_entry = Entry(root)
file_name_entry.place(relx = 0.5,rely = 0.1,anchor=CENTER)
text_area = Text(root,bg="grey70",fg="black")
text_area.place(relx = 0.5,rely = 0.6,anchor=CENTER)
#           <-- All Functions -->
name = ""
def openFile():
    try:
        global name
        text_area.delete(1.0,END)
        file_name_entry.delete(0,END)
        html_file = filedialog.askopenfilename(title=" Open HTML File", filetypes=(("HTML Files", "*.html"),))
        
        print(html_file)
        name = os.path.basename(html_file)
        actual_file_name = name.split(".")[0]
        print(actual_file_name)
        file_name_entry.insert(END,actual_file_name)
        root.title("HTML IDE: " + actual_file_name)
        html_file = open(html_file,'r')
        paragraph = html_file.read()
        text_area.insert(END,paragraph)
        html_file.close()
    except(FileNotFoundError):
        messagebox.showwarning("Warning","Please Open a File")
#            <-- All Buttons -->
open_button = Button(root,image = open_img ,command = openFile)
open_button.place(relx=0.3,rely=0.08)
save_button = Button(root,image = save_img)
save_button.place(relx=0.25,rely=0.08)
exit_button = Button(root,image = exit_img)
exit_button.place(relx=0.2,rely=0.08)
root.mainloop()