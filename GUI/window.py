from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk, Image
from eigenface import *
import numpy as np
import time
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

def btnstart() :
    starttime = time.time()
    default_size = [256,256]
    [X,y] = read_images(folderdirac,default_size)

    [eigenval,eigenvec,mean] = pca(as_row_matrix(X),y)

    T=[]

    numb = eigenvec.shape[1]
    for i in range (min(numb, 16)):
        e = eigenvec[:,i].reshape(X[0].shape )
        T.append(np.asarray(e))

    projections = []
    for xi in X:
        projections.append(project (eigenvec, xi.reshape(1 , -1) , mean))

    image = Image.open(filename)
    image = image.convert ("L")
    if (DEFAULT_SIZE is not None ):
        image = image.resize (DEFAULT_SIZE , Image.Resampling.LANCZOS )
    test_image = np. asarray (image , dtype =np. uint8 )
    predicted = predict(eigenvec, mean , projections, y, test_image)
    '''
    imeg = X[predicted]
    frame1 = Frame(window, width= 256, height= 256)
    frame1.pack()
    frame1.place(x= 951, y= 218, anchor=NW)

    labeldis = Label(frame1,image=imeg)
    labeldis.pack()
    '''
    endtime = time.time()
    tottime = endtime-starttime
    timez = str(tottime)
    canvas.itemconfig(TimeEx ,text = timez)



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
    command = btnstart,
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
