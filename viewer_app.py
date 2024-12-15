from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("learn how to code")
root.iconbitmap(r"C:\Users\aytur\Downloads\icon.ico")

my_img1= ImageTk.PhotoImage(Image.open("C:/Users/aytur/Desktop/images/images (1).jpg"))
my_img2= ImageTk.PhotoImage(Image.open("C:/Users/aytur/Desktop/images/images (2).jpg"))
my_img3= ImageTk.PhotoImage(Image.open("C:/Users/aytur/Desktop/images/images (3).jpg"))
my_img4= ImageTk.PhotoImage(Image.open("C:/Users/aytur/Desktop/images/images (4).jpg"))
my_img5= ImageTk.PhotoImage(Image.open("C:/Users/aytur/Desktop/images/images.jpg"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def button_all(request,image_number):
    global my_label
    global button_forward
    global button_back
    global label_num
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    if request=="forward":
        if image_number == len(image_list):
            button_forward = Button(root, text=">>", state=DISABLED)
        else:
            button_forward = Button(root, text=">>", command=lambda:button_all("forward",image_number + 1))
        button_back = Button(root, text="<<", command=lambda: button_all("back",image_number - 1))
    elif request=="back":
        if image_number == 1:
            button_back = Button(root, text="<<", state=DISABLED)
        else:
            button_back = Button(root, text="<<", command=lambda: button_all("back",image_number - 1))
        button_forward = Button(root, text=">>", command=lambda: button_all("forward",image_number + 1))
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    label_num.grid_forget()
    label_num=Label(root, text="Image {} in {}".format(image_number,len(image_list)),bd=1,relief="sunken")
    label_num.grid(row=2, column=2, columnspan=3)

button_back=Button(root,text="<<" ,state=DISABLED)
button_exit=Button(root,text="exit",command=root.quit)
button_forward=Button(root,text=">>",command=lambda:button_all("forward",2))

label_num=Label(root, text="Image 1 in {}".format(len(image_list)),bd=1,relief="sunken")
label_num.grid(row=2, column=2, columnspan=3)

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

root.mainloop()