import tkinter
from PIL import ImageTk, Image

from tkinter.filedialog import askdirectory

dirDataset = ''

def importDataset():
    global dirDataset
    global labeltest
    dirDataset = askdirectory()
    if labeltest:
        labeltest.destroy()
    labeltest = tkinter.Label(main_Win, text = dirDataset).pack()

main_Win = tkinter.Tk()

button1 = tkinter.Button(main_Win, text="Choose File", command = importDataset)
button1.pack()


main_Win.mainloop()