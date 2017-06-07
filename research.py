from Tkinter import *
# import client2 as c2
import tkFileDialog
#import first as f
# from PIL import ImageTk, Image

E1 = None
in_path=None
T1 = None
def close_window():
    global in_path
    in_path=E1.get()
#    f.main1(in_path)
    root.destroy()

def browser():
    global in_path
    in_path = tkFileDialog.askopenfilename()
    E1.insert(0, in_path)

def save():
    summary = T1.get()
    fp = open(in_path, "w");
    fp.write(summary)
    fp.close()


root = Tk()
#root.iconbitmap(default='transparent.ico')
root.wm_title("Paper Summerization")
root.geometry('650x300')
left_frame = Frame(root, height=300, width=250,borderwidth=5)
left_frame.pack_propagate(0)
left_frame.pack(side=LEFT)
right_frame = Frame(root, height=300, width=400,borderwidth=5)
right_frame.pack_propagate(0)
right_frame.pack(side=RIGHT)
client_frame = Frame(left_frame, height=30, width=250,borderwidth=5)
client_frame.pack_propagate(0)
client_frame.pack(side=TOP)
L_top = Label(client_frame, text="Research Paper Summarization",font=("Helvetica",12 ))
L_top.pack(side = TOP)
bottom_frame = Frame(left_frame, height=70, width=250)
bottom_frame.pack_propagate(0)
bottom_frame.pack(side=TOP)
L1 = Label(bottom_frame, text="UPLOAD\n",font=("Helvetica",12 ))
L1.pack(side = TOP)
textfield_frame = Frame(bottom_frame, height=40, width=200)
textfield_frame.pack_propagate(0)
textfield_frame.pack(side=TOP)
E1 = Entry(textfield_frame,width=50)
E1.place(x=10, y=10, width=100)
E1.pack(side = TOP)
#root.geometry('300x200')
button_frame = Frame(left_frame, height=80, width=250,borderwidth=20)
button_frame.pack_propagate(0)
button_frame.pack(side=TOP)
left_button_frame = Frame(button_frame, height=80, width=110,borderwidth=5)
left_button_frame.pack_propagate(0)
left_button_frame.pack(side=LEFT)
b = Button(left_button_frame, text="BROWSE", command=browser)
b.pack(side=LEFT)

right_button_frame = Frame(button_frame, height=80, width=140,borderwidth=5)
right_button_frame.pack_propagate(0)
right_button_frame.pack(side=RIGHT)
summ = Button(right_button_frame, text="SUMMARIZE", command=close_window)
summ.pack(side=LEFT)


summary_frame = Frame(right_frame, height=300, width=400,background = "white")
summary_frame.pack_propagate(0)
summary_frame.pack(side=TOP)
T1 = Text(summary_frame,width = 300,height = 400)
#E2.place(x=10, y=10, width=100)
T1.pack(side = TOP)
#img = ImageTk.PhotoImage(Image.open("image.jpg"))
#panel = Label(root, image = img)
#panel.pack(side = LEFT)

root.mainloop()
