from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk, Image

global new, imeg
def btn():
    print("Button Clicked")

def btn1():
    global new, imeg
    global filename
    filename = ''
    new = ''

    filename = filedialog.askopenfilename()
    head, tail = os.path.split(filename) # tail = nama file tanpa direct
    
    if tail != '' :
        copytail = tail # Buat display nama file tak lebih dari 22 char.
        if len(copytail) > 22 :
            copytail = copytail[:22]
        canvas.itemconfig(NoFileC, text = copytail)

        # Load image
        imeg = Image.open(filename)
        resized = imeg.resize((256,256), Image.ANTIALIAS)
        new = ImageTk.PhotoImage(resized)
        frame1 = Frame(window, width= 256, height= 256)
        frame1.pack()
        frame1.place(x= 402, y= 264, anchor=NW)

        labeldis = Label(frame1,image=new)
        labeldis.pack()

def btn2():
    global folderdirac, folderonly
    folderonly = ''
    folderdirac = ''

    folderdirac = filedialog.askdirectory() 
    # print(folderdirac)
    folderonly = os.path.basename(folderdirac)
    if folderonly != '' :
        copyfolnly = folderonly # Buat display nama folder tak lebih dari 22 char.
        if len(copyfolnly) > 22 :
            copyfolnly = copyfolnly[:22]
        canvas.itemconfig(NoFolC ,text = copyfolnly)
'''
def btnstart() :
    return 0 '''


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    640.0, 360.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn,
    relief = "flat")

b0.place(
    x = 701, y = 343,
    width = 234,
    height = 89)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn1,
    relief = "flat")

b1.place(
    x = 63, y = 530,
    width = 203,
    height = 62)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn2,
    relief = "flat")

b2.place(
    x = 63, y = 250,
    width = 203,
    height = 62)

NoFolC = canvas.create_text(155,333,
                            text="No Folder Chosen",
                            fill="#FFFFFF",
                            justify="left",
                            anchor="center",
                            font=("Comfortaa", 12))
                            
NoFileC = canvas.create_text(155,615,
                            text="No File Chosen",
                            fill="#FFFFFF",
                            justify="left",
                            anchor="center",
                            font=("Comfortaa", 12))       

TimeEx = canvas.create_text(575,598,
                            text="0 ms",
                            fill="#FFFFFF",
                            justify="left",
                            anchor="w",
                            font=("Comfortaa", 12))

Result = canvas.create_text(1020,595,
                            text="Belum Jalan Programnya",
                            fill="#FFFFFF",
                            justify="left",
                            anchor="w",
                            font=("Comfortaa", 12))

                             
window.resizable(False, False)
window.mainloop()
