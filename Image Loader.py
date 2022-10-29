import tkinter as tk
from PIL import ImageTk , Image

root=tk.Tk()
root.title("Image loader")
#WidthxHieght
root.geometry('500x300')

#width,height
root.minsize(300,180)
root.maxsize(800,600)

#labels
#only for JPEG image
a=input("enter the file name: ")
pic=Image.open(a)
photo=ImageTk.PhotoImage(pic)
label=tk.Label(image=photo)
label.pack()



#FOR OTHER TYPE OF IMAGE
'''
pic=tk.PhotoImage(file="filname")
label=tk.Label(image=pic)

'''
root.mainloop()