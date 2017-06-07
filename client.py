from Tkinter import *
import client2 as c2
from PIL import ImageTk, Image

def close_window():
    s=E1.get()
    root.destroy()
    c2.onbutton_click(s)

root = Tk()
root.iconbitmap(default='transparent.ico')
root.wm_title("Client ~ Server ~ Glances \'An Eye On Your Netwrok\'")
root.geometry('300x100')
client_frame = Frame(root, height=30, width=300,borderwidth=5)
client_frame.pack_propagate(0)
client_frame.pack(side=TOP)
L1 = Label(client_frame, text="Client Name",font=("Helvetica",12 ))
L1.pack(side = LEFT)
E1 = Entry(client_frame,width=50)
E1.pack(side = LEFT)
root.geometry('300x200')
button_frame = Frame(root, height=10, width=70)
button_frame.pack_propagate(0)
button_frame.pack(side=TOP)
b = Button(root, text="START", command=close_window)
b.pack(side=RIGHT)

img = ImageTk.PhotoImage(Image.open("image.jpg"))
panel = Label(root, image = img)
panel.pack(side = LEFT)

root.mainloop()