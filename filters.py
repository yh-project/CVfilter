from tkinter import *
from PIL import Image, ImageTk
import PIL
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
import cv2 as cv

# window open
tk = Tk()
tk.geometry('1500x700')

# filters btn frame
frame = LabelFrame(tk, text="필터 선택", padx=10, pady=10)
frame.place(x=10, y=10)

# input image frame
inputF = LabelFrame(tk, text="Input Image", padx=10, pady=10)
inputF.place(x=30, y=100, width=350, height=350)

inputLabel = Label(inputF)
inputLabel.pack()

# notice result
result = Image.open('./result_arrow.jpg')
result = result.resize((100, 100))
result = ImageTk.PhotoImage(result)

resultLabel = Label(tk, image=result)
resultLabel.place(x=430, y=225, width=100, height=100)

"""
Mean Filter
"""
# 3x3 result
m33result = LabelFrame(tk, text="3x3 Result", padx=10, pady=10)
m33result.place(x=580, y=100, width=350, height=350)

m33resultLabel = Label(m33result)
m33resultLabel.pack()

# 5x5 result
m55result = LabelFrame(tk, text="5x5 Result", padx=10, pady=10)
m55result.place(x=980, y=100, width=350, height=350)

m55resultLabel = Label(m55result)
m55resultLabel.pack()

def image_url():
    tk.filename = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(('all files', '*.*'), ('png files', '*.png'), ('jpg files', '*.jpg')))
    return tk.filename

def image_open(filter):
    global imgtk

    fn = image_url()

    img = cv.imread(fn, cv.IMREAD_GRAYSCALE)
    img = cv.resize(img, (300, 300))
    imgarr = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=imgarr)

    inputLabel.config(image=imgtk)
    if filter == "Mean":
        mean_filter(img)
        mean_filter(img, (5,5))
    elif filter == "Median":
        median_filter(img)
        median_filter(img, (5,5))

def mean_filter(img, filter_size=(3,3)):
    global meantk33
    global meantk55

    resImg = img
    oriImg = np.array(img)
    for i in range(int(filter_size[0]/2), int(300-filter_size[0]/2)):
        for j in range(int(filter_size[1]/2), int(300-filter_size[1]/2)):
            res = int(np.sum(oriImg[(i-int(filter_size[0]/2)):(i+int(filter_size[0]/2)+1), (j-int(filter_size[1]/2)):(j+int(filter_size[1]/2)+1)])/(filter_size[0] * filter_size[1]))
            resImg[i, j] = res

    imgarr = Image.fromarray(resImg)
    if filter_size[0] == 3: 
        meantk33 = ImageTk.PhotoImage(image=imgarr)
        m33resultLabel.config(image=meantk33)
    else:
        meantk55 = ImageTk.PhotoImage(image=imgarr) 
        m55resultLabel.config(image=meantk55)

def median_filter(img, filter_size=(3,3)):
    global mediantk33
    global mediantk55

    resImg = img
    oriImg = np.array(img)
    for i in range(int(filter_size[0]/2), int(300-filter_size[0]/2)):
        for j in range(int(filter_size[1]/2), int(300-filter_size[1]/2)):
            res = oriImg[(i-int(filter_size[0]/2)):(i+int(filter_size[0]/2)+1), (j-int(filter_size[1]/2)):(j+int(filter_size[1]/2)+1)]
            res = res.ravel()
            res = np.sort(res)
            resImg[i, j] = res[int((filter_size[0]*filter_size[1])/2)]

    imgarr = Image.fromarray(resImg)
    if filter_size[0] == 3:
        mediantk33 = ImageTk.PhotoImage(image=imgarr)
        m33resultLabel.config(image=mediantk33)
    else:
        mediantk55 = ImageTk.PhotoImage(image=imgarr)
        m55resultLabel.config(image=mediantk55)
   
meanBtn = Button(frame, text='Mean 필터', command=lambda: image_open("Mean"), width=12, height=1)
meanBtn.grid(row=0, column=0, padx=10)
medianBtn = Button(frame, text="Median 필터", command=lambda: image_open("Median"), width=12, height=1)
medianBtn.grid(row=0, column=1, padx=10)
laplacianBtn = Button(frame, text='Laplacian 필터', width=12, height=1)
laplacianBtn.grid(row=0, column=2, padx=10)
freeBtn = Button(frame, text='Choice 필터', width=12, height=1)
freeBtn.grid(row=0, column=3, padx=10)

tk.mainloop()