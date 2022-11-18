from tkinter import *
from PIL import Image, ImageTk
import PIL
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
import cv2 as cv

state5 = True
curfilter = "Mean"

# window open
tk = Tk()
tk.geometry('1500x900')
tk.title('Spacial Filters')

# filters btn frame
frame = LabelFrame(tk, text="필터 선택", padx=10, pady=10)
frame.place(x=10, y=10)

# input image frame
inputF = LabelFrame(tk, text="Input Image", padx=10, pady=10)
inputF.place(x=30, y=100, width=350, height=350)

inputLabel = Label(inputF)
inputLabel.pack()

# notice result
result = Image.open('./image/result_arrow.jpg')
result = result.resize((100, 100))
result = ImageTk.PhotoImage(result)

resultLabel = Label(tk, image=result)
resultLabel.place(x=430, y=225, width=100, height=100)

"""
Filter
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

"""
Option
"""
# option
optionFrame = LabelFrame(tk, text="Option")
optionFrame.place(x=30, y=500, width=350, height=350)

kMent = Label(optionFrame, text="필터 사이즈(n * n)")
kMent.place(x=50, y=30, width=100, height=20)

kInput = Entry(optionFrame)
kInput.place(x=200, y=30, width=100, height=20)

sMent = Label(optionFrame, text="스케일(default=1)")
sMent.place(x=50, y=70, width=100, height=20)

sInput = Entry(optionFrame)
sInput.place(x=200, y=70, width=100, height=20)

dMent = Label(optionFrame, text="델타(default=1)")
dMent.place(x=50, y=110, width=100, height=20)

dInput = Entry(optionFrame)
dInput.place(x=200, y=110, width=100, height=20)

rBtn = Button(optionFrame, text="옵션 적용", command=lambda: image_open("Option"))
rBtn.place(x=50, y=290, width=250, height=30)

# option notice result
oresult = Image.open('./image/result_arrow.jpg')
oresult = oresult.resize((100, 100))
oresult = ImageTk.PhotoImage(oresult)

oresultLabel = Label(tk, image=result)
oresultLabel.place(x=430, y=625, width=100, height=100)

# option result
optionresult1 = LabelFrame(tk, text="Option Result1", padx=10, pady=10)
optionresult1.place(x=580, y=500, width=350, height=350)

optionresult1Label = Label(optionresult1)
optionresult1Label.pack()

optionresult2 = LabelFrame(tk, text="Option Result2", padx=10, pady=10)
optionresult2.place(x=980, y=500, width=350, height=350)

optionresult2Label = Label(optionresult2)
optionresult2Label.pack()

optionresult2Label.pack_forget()
optionresult2.place_forget()

def type_check(type):
    global state5

    if type == "low-pass":
        if state5 == "high":
            m55result.place(x=980, y=100, width=350, height=350)
            m55resultLabel.pack()
        elif state5 == "roberts-prewitt-sobel":
            optionresult2Label.pack_forget()
            optionresult2.place_forget()
            optionresult1.config(text='Option Result')
            m33result.config(text='3x3 Result')
            m55result.config(text='5x5 Result')
        optionresult1Label.config(image='')
        optionresult2Label.config(image='')
        state5 = "low"
    elif type == "high-pass":
        if state5 == "roberts-prewitt-sobel":
            m33result.config("3x3 Result")
            optionresult2Label.pack_forget()
            optionresult2.place_forget()
            optionresult1.config(text='Option Result')
        m55resultLabel.pack_forget()
        m55result.place_forget()
        optionresult1Label.config(image='')
        optionresult2Label.config(image='')
        state5 = "high"
    elif type == "roberts-prewitt-sobel":
        if state5 == "high":
            m55result.place(x=980, y=100, width=350, height=350)
            m55resultLabel.pack()
        m33result.config(text='x 방향 미분')
        m55result.config(text='y 방향 미분')
        optionresult2.place(x=980, y=500, width=350, height=350)
        optionresult2Label.pack()
        optionresult1.config(text='x 방향 Option')
        optionresult2.config(text='y 방향 Option')
        optionresult1Label.config(image='')
        optionresult2Label.config(image='')
        state5 = "roberts-prewitt-sobel"

def image_url():
    tk.filename = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(('all files', '*.*'), ('png files', '*.png'), ('jpg files', '*.jpg')))
    return tk.filename

def image_open(filter):
    global imgtk
    global curfilter
    global imgs

    if filter != "Option":
        fn = image_url()

        imgs = cv.imread(fn, cv.IMREAD_GRAYSCALE)
        imgs = cv.resize(imgs, (300, 300))
        imgarr = Image.fromarray(imgs)
        imgtk = ImageTk.PhotoImage(image=imgarr)

        inputLabel.config(image=imgtk)
    
    if filter == "Mean":
        curfilter = "Mean"
        type_check("low-pass")
        mean_filter(imgs)
        mean_filter(imgs, (5,5))
    elif filter == "Median":
        curfilter = "Median"
        type_check("low-pass")
        median_filter(imgs)
        median_filter(imgs, (5,5))
    elif filter == "Laplacian":
        curfilter = "Laplacian"
        type_check("high-pass")
        laplacian_filter(imgs, "Original")
    elif filter == "Roberts":
        curfilter = "Roberts"
        type_check("roberts-prewitt-sobel")
        roberts_filter(imgs)
    elif filter == "Sobel":
        curfilter = "Sobel"
        type_check("roberts-prewitt-sobel")
        sobel_filter(imgs)
    elif filter == "Prewitt":
        curfilter = "Prewitt"
        type_check("roberts-prewitt-sobel")
        prewitt_filter(imgs)
    elif filter == "Option":
        if curfilter == "Mean":
            mean_filter(imgs, (int(kInput.get()),int(kInput.get())))
        elif curfilter == "Median":
            median_filter(imgs, (int(kInput.get()),int(kInput.get())))
        elif curfilter == "Laplacian":
            laplacian_filter(imgs, "Option", ksize=int(kInput.get()), scale=int(sInput.get()), delta=int(dInput.get()))
        elif curfilter == "Sobel":
            sobel_filter(imgs, "Option", (int(kInput.get()),int(kInput.get())))

def mean_filter(img, filter_size=(3,3)):
    global meantk33
    global meantk55
    global meantknn

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
    elif filter_size[0] == 5:
        meantk55 = ImageTk.PhotoImage(image=imgarr) 
        m55resultLabel.config(image=meantk55)
    else:
        meantknn = ImageTk.PhotoImage(image=imgarr)
        optionresult1Label.config(image=meantknn)


def median_filter(img, filter_size=(3,3)):
    global mediantk33
    global mediantk55
    global mediantknn

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
    elif filter_size[0] == 5:
        mediantk55 = ImageTk.PhotoImage(image=imgarr)
        m55resultLabel.config(image=mediantk55)
    else:
        mediantknn = ImageTk.PhotoImage(image=imgarr)
        optionresult1Label.config(image=mediantknn)
   
def laplacian_filter(img, type, ksize=3, scale=1, delta=1):
    global laplaciantk33
    global laplaciantknn

    resImg = cv.Laplacian(img, -1, ksize=ksize, scale=scale, delta=delta)
    imgarr = Image.fromarray(resImg)

    if type == "Original":
        laplaciantk33 = ImageTk.PhotoImage(image=imgarr)
        m33resultLabel.config(image=laplaciantk33)
    elif type == "Option":
        laplaciantknn = ImageTk.PhotoImage(image=imgarr)
        optionresult1Label.config(image=laplaciantknn)

def roberts_filter(img):
    global xrobertstk33
    global yrobertstk33

    roberts_x = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 0]])
    roberts_y = np.array([[0, 0, -1], [0, 1, 0], [0, 0, 0]])    

    roberts_x = cv.convertScaleAbs(cv.filter2D(img, -1, roberts_x))
    roberts_y = cv.convertScaleAbs(cv.filter2D(img, -1, roberts_y))

    ximgarr = Image.fromarray(roberts_x)
    yimgarr = Image.fromarray(roberts_y)

    xrobertstk33 = ImageTk.PhotoImage(image=ximgarr)
    yrobertstk33 = ImageTk.PhotoImage(image=yimgarr)

    m33resultLabel.config(image=xrobertstk33)
    m55resultLabel.config(image=yrobertstk33)

def sobel_filter(img, type="Original", filter_size=(3,3)):
    global xsobeltk33
    global ysobeltk33
    global xsobeltknn
    global ysobeltknn

    sobel_x = cv.Sobel(img, -1, 1, 0, ksize=filter_size[0])
    sobel_y = cv.Sobel(img, -1, 0, 1, ksize=filter_size[1])

    ximgarr = Image.fromarray(sobel_x)
    yimgarr = Image.fromarray(sobel_y)

    if type == "Original":
        xsobeltk33 = ImageTk.PhotoImage(image=ximgarr)
        ysobeltk33 = ImageTk.PhotoImage(image=yimgarr)
        m33resultLabel.config(image=xsobeltk33)
        m55resultLabel.config(image=ysobeltk33)
    elif type == "Option":
        xsobeltknn = ImageTk.PhotoImage(image=ximgarr)
        ysobeltknn = ImageTk.PhotoImage(image=yimgarr)
        optionresult1Label.config(image=xsobeltknn)
        optionresult2Label.config(image=ysobeltknn)

def prewitt_filter(img):
    global xprewitttk33
    global yprewitttk33

    prewitt_x = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    prewitt_y = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])

    prewitt_x = cv.convertScaleAbs(cv.filter2D(img, -1, prewitt_x))
    prewitt_y = cv.convertScaleAbs(cv.filter2D(img, -1, prewitt_y))

    ximgarr = Image.fromarray(prewitt_x)
    yimgarr = Image.fromarray(prewitt_y)

    xprewitttk33 = ImageTk.PhotoImage(image=ximgarr)
    yprewitttk33 = ImageTk.PhotoImage(image=yimgarr)

    m33resultLabel.config(image=xprewitttk33)
    m55resultLabel.config(image=yprewitttk33)
    
meanBtn = Button(frame, text='Mean 필터', command=lambda: image_open("Mean"), width=12, height=1)
meanBtn.grid(row=0, column=0, padx=10)
medianBtn = Button(frame, text="Median 필터", command=lambda: image_open("Median"), width=12, height=1)
medianBtn.grid(row=0, column=1, padx=10)
laplacianBtn = Button(frame, text='Laplacian 필터', command=lambda: image_open("Laplacian"), width=12, height=1)
laplacianBtn.grid(row=0, column=2, padx=10)
roberts = Button(frame, text='Robert 필터', command=lambda: image_open("Roberts"), width=12, height=1)
roberts.grid(row=0, column=3, padx=10)
sobel = Button(frame, text='Sobel 필터', command=lambda: image_open("Sobel"), width=12, height=1)
sobel.grid(row=0, column=4, padx=10)
prewitt = Button(frame, text='Prewitt 필터', command=lambda: image_open("Prewitt"), width=12, height=1)
prewitt.grid(row=0, column=5, padx=10)

tk.mainloop()