from tkinter import *
import tkinter as tk
import PIL
from PIL import ImageTk, Image
import glob
import os

# --- functions ---

i = 0
img=0
imagelist=[]
imagelistname=[]
path = 'injest/'
equipnumberentry = ""
imagelableentry = "" 
imageorderentry = ""
yup=""


def text_mod():
    global i, btn2, imagelist, image, imagelistname, yup         # btn can be omitted but not sure if should be
    btn2['text'] = imagelistname[i]    # the global object that is modified
    yup = imagelistname[i]
    photo = load_images()
    i = (i + 1) % len(imagelistname)  # another global object that gets modified
    item4 = canvas.create_image(209, 164, image=photo)
    root.mainloop()

def load_images():
    global i, btn2, imagelist, image,imagelistname, yup
    image = Image.open(yup)
    basewidth = 900
    #wpercent = (basewidth / float(image.size[0]))
    #hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((418,328), PIL.Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    return photo

def resize_Image(simage):
    im = Image.open(simage)
    if im.width != 318 and im.height != 228:
        resized_im = im.resize((318,228))
        resized_im.save(simage)

def injest_image():
    global imagelableentry, imageorderentry, imagelistname, equipnumberentry, yup
    im = Image.open(yup)
    if im.width != 318 and im.height != 228:
        im = im.resize((318,228))
        s1=str(equipnumberentry.get())
        s2=str(imagelableentry.get())
        s3=str(imageorderentry.get())
        if not os.path.exists("images/"+s1):
            os.makedirs("images/"+s1)

        im.save("images/"+s1+"/"+s2+" "+str(s3)+".jpg")
        os.rename(yup, "injest/done/"+yup)
        imagelistname.remove(yup)
def image_reload():
    global imagelist, imagelistname
    imagelistname=[]
    imagelist=[]
    for filename in glob.glob(path+'/*.jpg'): #assuming gif
        im=Image.open(filename)
        imagelist.append(im)
        imagelistname.append(filename)
root=Tk()


for filename in glob.glob(path+'/*.jpg'): #assuming gif
    im=Image.open(filename)
    imagelist.append(im)
    imagelistname.append(filename)

canvas=Canvas(root, height=330, width=1000)

eqnlable = tk.Label(root, text='Equipment Number:')
eqnlable.config(font=('helvetica', 10))
canvas.create_window(550, 140, window=eqnlable)
equipnumberentry = tk.Entry (root) 
canvas.create_window(680, 140, window=equipnumberentry)

imglable = tk.Label(root, text='Image lable:')
imglable.config(font=('helvetica', 10))
canvas.create_window(550, 160, window=imglable)
imagelableentry = tk.Entry (root) 
canvas.create_window(680, 160, window=imagelableentry)

imgorder = tk.Label(root, text='Image order ( 1-6 ):')
imgorder.config(font=('helvetica', 10))
canvas.create_window(550, 180, window=imgorder)
imageorderentry = tk.Entry (root) 
canvas.create_window(680, 180, window=imageorderentry)

btn = tk.Button(root, text="Reload Image List", height=1)
btn['command'] = injest_image

btn = tk.Button(root, text="Injest Image", height=2, width = 20)
btn['command'] = image_reload

btn2 = tk.Button(root, text="Cycle Images",height=2)
btn2['command'] = text_mod

btn.pack(fill='both', expand=True)
btn.place(x=600, y=300)
btn2.pack(fill='both', expand=True)
canvas.pack(side = TOP, expand=True, fill=BOTH)
root.mainloop()

