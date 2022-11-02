from tkinter import *
from PIL import Image, ImageTk
import PIL
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
import cv2 as cv

'''
tk = Tk()
tk.title('Spatial Filtering')
tk.geometry('1000x1000')

def image_url():
    tk.filename = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))
    return tk.filename

def image_open():
    fn = image_url()
    
    image = Image.open(fn)

    canvas = Canvas(tk, height=500, width=500)
    image = image.resize((500, 500), PIL.Image.Resampling.LANCZOS)

    real_image = ImageTk.PhotoImage(image)
    print(tk.filename)
    return canvas, real_image

def print_image():
    canvas, real_image = image_open()
    item4 = canvas.create_image(250, 250, image=real_image)
    canvas.pack()

#canvas, real_image = image_open()
#item4 = canvas.create_image(250, 250, image=real_image)
#canvas.pack()

#print(real_image)
    
my_btn = Button(tk, text='파일열기', command=image_open).pack()
 
tk.mainloop()
'''




tk = Tk()
tk.geometry('1500x700')

frame = LabelFrame(tk, text="필터 선택", padx=10, pady=10)
frame.pack(side="top")
#frame.grid(row=0, column=0, padx=10, pady=10)

resultF = LabelFrame(tk, text="실행 결과", padx=10, pady=10)
resultF.pack()

inputF = LabelFrame(resultF, text="Input Image", padx=10, pady=10)
inputF.grid(row=0, column=0)
#inputF.grid(row=1, column=0, sticky="W", padx=10, pady=10)

inputLabel = Label(inputF)
inputLabel.pack()

sexLabel = Label(resultF, text="sibal")
sexLabel.grid(row=0, column=1)

def image_url():
    tk.filename = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(('all files', '*.*'), ('png files', '*.png'), ('jpg files', '*.jpg')))
    return tk.filename

def image_open():
    global imgtk

    fn = image_url()
    print(fn)

    img = cv.imread(fn, cv.IMREAD_GRAYSCALE)
    img = cv.resize(img, (300, 300))
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img)

    inputLabel.config(image=imgtk)

meanBtn = Button(frame, text='Mean 필터', command=lambda: image_open(), width=12, height=1)
meanBtn.grid(row=0, column=0, padx=10)
medianBtn = Button(frame, text="Median 필터", width=12, height=1)
medianBtn.grid(row=0, column=1, padx=10)
laplacianBtn = Button(frame, text='Laplacian 필터', width=12, height=1)
laplacianBtn.grid(row=0, column=2, padx=10)
freeBtn = Button(frame, text='Choice 필터', width=12, height=1)
freeBtn.grid(row=0, column=3, padx=10)




tk.mainloop()























def median_filter(img, filter_size=(3,3), stride=1):
    img_shape = np.shape(img)

    result_shape = tuple(np.int64((np.array(img_shape)-np.array(filter_size))/stride+1))
    result = np.zeros(result_shape)

    for h in range(0, result_shape[0], stride):
        for w in range(0, result_shape[1], stride):
            tmp = img[h:h+filter_size[0], w:w+filter_size[1]]
            tmp = np.sort(tmp.ravel())
            result[h,w] = tmp[int(filter_size[0]*filter_size[1]/2)]

    return result

def show(img, max_ylim=12500):
    
    plt.imshow(img, cmap='gray')
    plt.show()
    
    if max_ylim != 'none':
        axes = plt.axes()
        axes.set_ylim([0, max_ylim])
    plt.hist(img.ravel(), bins=256, range=[0,256])
    plt.show()