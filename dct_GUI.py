# C:\Users\ricca\Desktop\artificial.bmp
# file picker
from tkinter import messagebox
from tkinter import *
import cv2
from fft import *
from scipy.misc import imsave


def show_message():
    messagebox.showinfo("Error", "\u03B2 should be from 0 to N+M-2")


def fix_values(ff):
    cols = ff.shape[0]
    rows = ff.shape[1]
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
    cols = c.shape[0]
    rows = c.shape[1]
    for i in range(rows):
        for j in range(cols):
            if i+j >= d:
                c[i, j] *= beta

    ff = fft_idct_2d(c)
    return ff


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
    c = fft_dct_2d(f)
    ff = beta_mult(d, beta, c)
    ff = fix_values(ff)

    imsave('prova', ff)






    # print('You clicked the button!')
    # print(img_path)
    # print(d)
    # print(matrix)


top = Tk()

label_transparent = Label(top, text='')
label_transparent.grid(row=0, column=0)

# PATH
Path_label = Label(top, text="Image Path: ")
Path_label.grid(row=1, column=0)
Path_entry = Entry(top, bd=5, width=50)
Path_entry.grid(row=1, column=1)

# D VALUE
D_label = Label(top, text="Value d: ")
D_label.grid(row=2, column=0)
D_entry = Entry(top, bd=5)
D_entry.grid(row=2, column=1, sticky='we')


# B VALUE
beta_label = Label(top, text="Value \u03B2: ")
beta_label.grid(row=3, column=0)
beta_entry = Entry(top, bd=5)
beta_entry.grid(row=3, column=1, sticky='we')

MyButton1 = Button(top, text="Submit", width=20, height=3, command=callback)
MyButton1.grid(row=2, column=4)

top.grid_columnconfigure(4, minsize=200)
top.grid_rowconfigure(4, minsize=50)




top.mainloop()



# from tkinter import *
#
# window = Tk()
# User_input = Entry()
# User_input.pack()
#
#
# window.mainloop()
#
# user_problem = int(User_input.get())
#
# print('aaa')

# root = Tk()
#
# mypattern = [('BMP', '*.bmp')]
#
#
# class Application(Frame):
#
#     def say_hi(self):
#         print("hi there, everyone!")
#
#     # def myfileOpen(self):
#     #     self.myfile = Tk.filedialog.askopenfile(filetypes='*.bmp',
#     #                                             title='Open a Python file', mode='r')
#     #     loadedfile = self.myfile.read()
#     #     self.myfile.close()
#     #     self.textView.insert("end", loadedfile)
#
#
#     # def retrieve_input():
#     #     input = self.myText_Box.get("1.0", END)
#
#     def createWidgets(self):
#         self.QUIT = Button(self)
#         self.QUIT["text"] = "QUIT"
#         self.QUIT["fg"] = "red"
#         self.QUIT["command"] = self.quit
#
#         self.QUIT.pack({"side": "left"})
#
#         self.hi_there = Button(self)
#         self.hi_there["text"] = "Hello",
#         self.hi_there["command"] = self.say_hi
#
#         self.hi_there.pack({"side": "left"})
#
#         self.myfile = Tk.filedialog.askopenfile(filetypes=mypattern, title='Open a Python file', mode='r')
#         loadedfile = self.myfile.read()
#         self.myfile.close()
#         self.textView.insert("end", loadedfile)
#
#
#
#
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#
#
#
#
#
# #root = Tk()
#
# app = Application(master=root)
# app.mainloop()
# root.destroy()
