# C:\Users\ricca\Desktop\artificial.bmp
from tkinter import *
import cv2
import numpy as np



def callback():
    img_path = E1.get()
    print(img_path)
    img = cv2.imread(img_path, 0)
    matrix = np.array(img, dtype=float)
    print('You clicked the button!')
    print(matrix)

top = Tk()
L1 = Label(top, text="Image Path: ")
L1.grid(row=0, column=0)
E1 = Entry(top, bd=5)
E1.grid(row=0, column=1)

MyButton1 = Button(top, text="Submit", width=10, command=callback)
MyButton1.grid(row=1, column=1)



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
