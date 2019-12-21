
from tkinter import *

root=Tk() # membuat window
root.iconbitmap("icon/icon.ico") # merubah icon
root.geometry('326x45') # merubah ukuran window
root.title('Face Recognition') # Merubah judul

#####################    MEMBUAT FUNGSI TOMBOL KETIKA DI TEKAN     #####################
def detect():
    print("Detect")
def new():
    print("New")
def training():
    print("Training")
def openFile():
    print("Open files")

#======================================================================================#
#                             MEMBUAT TOMBOL BERGAMBAR                                 #
#======================================================================================#
# tombol uji face recognition
img_detect = PhotoImage(file="img/face_detec.png").subsample(15, 15)
btn_detect = Button(root, image=img_detect, compound=LEFT, command=detect, text='Detect').pack(side=LEFT)

# tombol untuk menambahkan data
img_new = PhotoImage(file="img/add_data.png").subsample(15, 15)
btn_new = Button(root, image=img_new, compound=LEFT, command=new, text='New').pack(side=LEFT)

# tombol untuk includ data training
img_training = PhotoImage(file="img/training.png").subsample(15, 15)
btn_training = Button(root, image=img_training, compound=LEFT, command=training, text='Training').pack(side=LEFT)

# tombol untuk melihat data training
img_open_file = PhotoImage(file="img/files.png").subsample(15, 15)
btn_open_file = Button(root, image=img_open_file, compound=LEFT, command=openFile, text='Open file').pack(side=LEFT)

root.mainloop()