from tkinter import messagebox, filedialog
from tkinter import ttk
from tkinter import *
import cv2
from fft import *
from scipy.misc import imsave
import matplotlib.pyplot as plt
import os


# messaggio di errore per il valore 'd'
def show_message():
    messagebox.showinfo("Error", "Value 'd' should be from 0 to N+M-2")


# setta i valori come richiesto
def fix_values(ff):
    rows = ff.shape[0]
    cols = ff.shape[1]
    for i in range(rows):
        for j in range(cols):
            if ff[i,j] < 0:
                ff[i,j]=0       # setto a 0 i valori negativi
            elif ff[i,j] > 255:
                ff[i,j] = 255   # setto a 255 i valori maggiori di 255
            else:
                ff[i,j] = int(round(ff[i,j]))
    return ff


# moltiplica per il coeffciente beta le frequenze c(k,l) con k+l>=d
def beta_mult(d, beta, c):
    rows = c.shape[0]
    cols = c.shape[1]
    for i in range(rows):
        for j in range(cols):
            if i+j >= d:
                c[i, j] *= beta

    ff = fft_idct_2d(c)
    return ff


# metodo lanciato quando si preme il bottone 'Start'
def callback():
    img_path = Path_entry.get()
    d = int(D_entry.get())
    beta = int(beta_entry.get())
    img = cv2.imread(img_path, 0)
    f = np.array(img, dtype='float64')
    cols = f.shape[0]
    rows = f.shape[1]
    if d < 0 or d > (rows + cols - 2):
        show_message()
    else:
        mpb["value"] = 25
        root.update()
        c = fft_dct_2d(f)
        mpb["value"] = 50
        root.update()
        ff = beta_mult(d, beta, c)
        mpb["value"] = 75
        root.update()
        ff = fix_values(ff)
        mpb["value"] = 95
        root.update()
        imsave('final.jpg', ff)
        mpb["value"] = 100

        plt.figure(1)
        # plt.subplot(121)
        plt.subplot(121)
        # plt.imshow(f, cmap='gray', vmin=0, vmax=255)
        plt.imshow(f, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

        # final = cv2.imread('final.jpg', 0)
        plt.subplot(122) # 122
        # plt.imshow(ff, cmap='gray', vmin=0, vmax=255)
        plt.imshow(ff, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

        plt.show()


# apre il file picker per scegliere l'immagine
def browse():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select BMP File", filetypes=[("BMP Files", "*.bmp")])
    Path_entry.insert(END, filename)


root = Tk()


label_transparent = Label(root, text='')
label_transparent.grid(row=0, column=0)

# PATH
Path_label = Label(root, text="Image Path: ")
Path_label.grid(row=1, column=0)
Path_entry = Entry(root, bd=5, width=50)
Path_entry.grid(row=1, column=1)

# D VALUE
D_label = Label(root, text="Value d: ")
D_label.grid(row=2, column=0)
D_entry = Entry(root, bd=5)
D_entry.grid(row=2, column=1, sticky='we')


# B VALUE
beta_label = Label(root, text="Value \u03B2: ")
beta_label.grid(row=3, column=0)
beta_entry = Entry(root, bd=5)
beta_entry.grid(row=3, column=1, sticky='we')

# START BUTTON
Start_button = Button(root, text="Start", width=20, height=3, command=callback)
Start_button.grid(row=5, column=1)

# BROWSE BUTTON
Browse_button = Button(root, text="Browse", width=20, command=browse)
Browse_button.grid(row=1, column=4)


# PROGRESS BAR
mpb = ttk.Progressbar(root,orient ="horizontal",length = 300, mode ="determinate")
mpb["maximum"] = 100
mpb.grid(row=6, column=1)

root.title("DCT")

root.grid_columnconfigure(4, minsize=200)
root.grid_rowconfigure(6, minsize=50)

root.mainloop()
